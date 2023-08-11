import logging

import azure.functions as func
import pandas as pd
import io
#import json
import json_normalize
from azure.storage.blob import BlobServiceClient


def main(myblob: func.InputStream):
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Crear el cliente del servicio de Blob
    blob_service_client = BlobServiceClient(account_url=f"https://proyectofinalgrupo05.blob.core.windows.net/", credential='vrh6zC8lshFY666G21tX7B5jFBsTKcEpv90E6ttyPVnbckIheKpL3zSnNOse9YrTSoHmtULIcSEu+ASt0qK2EA==')

    # Obtener una referencia al contenedor
    container_client = blob_service_client.get_container_client('users')

    # Download the blob to a pandas DataFrame
    data = myblob.read()
    #data = blob_client.download_blob().readall()
    df = pd.read_json(io.BytesIO(data))
    
    # Perform transformation
    # Normalizar la columna "reviews" en nuevas columnas
    df = json_normalize(df, record_path="reviews", meta=["total", "possible_languages"])

    df['text'] = df['text'].replace("\W", ' ', regex=True)
    df['text'] = df['text'].replace("  ", ' ', regex=True)

    # Crear el nuevo DataFrame df_final
    df_transformed = df[['user.id', 'rating', 'time_created', 'text']]

    # Get the output blob
    #blob_client = blob_service_client.get_blob_client('users', 'YelpApi_Test.csv')
    blob_client = container_client.get_blob_client('YelpApi_Test.csv')    
    
    # Upload the transformed DataFrame to the output blob
    output = io.StringIO()
    df_transformed.to_csv(output, index=False)
    output_blob = output.getvalue()
    blob_client.upload_blob(output_blob, overwrite=True)
