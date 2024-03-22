# UploadX: File Upload on Minio Server using Flask

"UploadX" showcases the integration of Flask and Minio for effortless file uploads to a local Minio instance. Users can easily manage and download recently or previously uploaded files through a clean and intuitive interface. 

## Installation

To install the project, clone the repository and navigate to the project directory:
```bash
git clone github.com/psankhe28/minio-demo.git

cd minio-demo
```
    
Run the minio.

```bash
docker-compose up --build
```
Minio is running with follwoing username and password.
```bash
localhost:9001
username: minioadmin
password: minioadmin
```

Install and run the flask app. 
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

Using Thunderclient/Postman for uploading file using following URL.
(POST request)
```bash
localhost:5000/upload
```

Using Thunderclient/Postman for downloading file locally using following URL.
(GET request)

```bash
localhost:5000//download/<filename>
```
