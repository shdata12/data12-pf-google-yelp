from azure.storage.blob import BlobServiceClient
import pandas as pd
import json_normalize


def preprocess(df: pd.DataFrame):
   """
   Preprocess the given dataframe by extracting
   user.id - rating - time_created - text
   del archivo json original.
   :returns: The new dataframe.
   """
   # Perform transformation
   # Normalizar la columna "reviews" en nuevas columnas
   df = json_normalize(df, record_path="reviews", meta=["total", "possible_languages"])

   df['text'] = df['text'].replace("\W", ' ', regex=True)
   df['text'] = df['text'].replace("  ", ' ', regex=True)

   # Crear el nuevo DataFrame df_final
   df_transformed = df[['user.id', 'rating', 'time_created', 'text']]
   return df

def save_dataframe_to_blob(df: pd.DataFrame, connection_string: str, container_name: str, blob_name: str):
   """
   Saves a dataframe to azure blob storage.
   :param df: The dataframe to be saved.
   :param connection_string: The blob storage connection string.
   :param container_name: The container name.
   :param blob_name: The file name. 
   """
   connection_string = "DefaultEndpointsProtocol=https;AccountName=henrypfdatalake;AccountKey=q0lWZah2r7VyThDfb1v6r9E1hROKDSrzFoyRkKRe/6Ic0dkzDdf3XBDwamxmMHVmR11dHP40W89y+ASt+PxMuw==;EndpointSuffix=core.windows.net"
   # Convert the DataFrame to a CSV string
   csv_data = df.to_csv(index=False)

   # Create a BlobServiceClient object
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)

   # Create a ContainerClient object
   container_client = blob_service_client.get_container_client(container_name)

   # Create a blob client and upload the CSV data
   blob_client = container_client.get_blob_client(blob_name)
   blob_client.upload_blob(csv_data, overwrite=True)