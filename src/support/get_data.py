import os
import wget
import zipfile

url = 'https://datasets.simula.no/kvasir/data/kvasir-dataset-v2.zip'
zip_name = "data.zip"

wget.download(url, zip_name)

# Unzip it and standardize the .csv filename

with zipfile.ZipFile(zip_name,"r") as zip_ref:
    zip_ref.extractall(path='../../data/')

os.remove(zip_name)
