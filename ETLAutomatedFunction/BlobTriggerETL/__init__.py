import logging

import azure.functions as func
import pandas as pd
from io import BytesIO
import os
from azure.storage.blob import BlobServiceClient
from .utilities import preprocess, save_dataframe_to_blob
import time


def main(myblob: func.InputStream):
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Crear el cliente del servicio de Blob
    #blob_service_client = BlobServiceClient(account_url=f"https://henrypfdatalake.blob.core.windows.net/", credential='YwjSsI65leR48quFvo66Jd4oz55sW2PdWraepJLStf/evzW2/ks9aWZMlixxph/BWQO6OiH5GcNB+ASt6YaFvw==')

    # Obtener una referencia al contenedor
    #container_client = blob_service_client.get_container_client('users')

    # Converting the json file to dataframe 
    df = pd.read_json(BytesIO(myblob.read()))
    
    # Preprocessing the data
    df = preprocess(df)
    
    # Preparing the file name
    blob_name = myblob.name.split("/")[-1].split(".")[0]
    file_name = f"{blob_name}_{int(time.time())}_preprocessed.csv"

    # Saves the data to Azure blob storage
    save_dataframe_to_blob(df, os.environ.get("henrypfdatalake_STORAGE"), "users", file_name)