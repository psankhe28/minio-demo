from flask import Flask, request, send_file, render_template
from minio import Minio
import os
import io
import mimetypes
app = Flask(__name__)

BUCKET_NAME = 'mybuck'
minio_client = Minio("localhost:9000",
    access_key='kf63ySXOPUtCzt5f',
    secret_key='PN561uS3b51GMFkAOvZ1fJbrjWdhwc2o',
    secure=False)

@app.route('/upload', methods=['POST'])
def upload():
       
    try:
        minio_client.make_bucket(BUCKET_NAME)
    except:
        pass
    
    file = request.files['file']
    filename = file.filename
    print("--"*20)
    print(filename)
    print("--"*20)
    file_data = io.BytesIO(file.stream.read())
    minio_client.put_object(
        bucket_name=BUCKET_NAME,
        object_name=filename,
        data=file_data,
        length=len(file_data.getbuffer()),
        content_type=file.content_type,
    )
    

    return f'File uploaded to MinIO! {filename} '

@app.route('/download/<filename>')
def download(filename):
    try:
        data = minio_client.get_object(
            bucket_name=BUCKET_NAME,
            object_name=filename,
        )
        
        mime_type, _ = mimetypes.guess_type(filename)
        return send_file(
            io.BytesIO(data.read()),
            as_attachment=True,
            download_name=filename,
            mimetype=mime_type
        )
    except Exception as e:
        return f'File not found in MinIO!  {e}'
    
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)