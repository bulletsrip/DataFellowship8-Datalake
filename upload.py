import os
import wget
from google.cloud import storage

# Variable
project_id = 'datafellowship-370013'
bucket_name = 'df8'
bucket_file = 'test'
source_file_name = 'https://www.gstatic.com/devrel-devsite/prod/vc82f2cad3fcff18d6946c0a512e7dbee1d0b7079276de2cee506a18bb2ccb908/cloud/images/social-icon-google-cloud-1200-630.png' 

# Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'application_default_credentials.json'

# Instantiates a client
try:
    file_name = wget.download(source_file_name)
    client = storage.Client(project_id)                   
    bucket = client.get_bucket(bucket_name)     
    blob = bucket.blob(bucket_file)             
    blob.upload_from_filename(file_name, content_type='image/jpg')

    print(f"{bucket_file} Has been uploaded to Google Cloud Storage")
except Exception as e:
    print(e)

