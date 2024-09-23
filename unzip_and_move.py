import os
import zipfile
from datetime import timedelta, datetime

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

zip_filenames = {
    "caddy": yesterday + "-catalogdata-caddy.zip",
    "erico": yesterday + "-catalogdata-erico.zip",
}

path_to_zip = "F:\\P360Data\\NightlyP360Data"
path_to_temp = "F:\\P360Data\\temp"

with zipfile.ZipFile(path_to_zip + '\\' + zip_filenames['caddy']) as f:
    print("Extracting Files")
    f.extractall(path_to_temp)

#print(path_to_zip + '\\' + zip_filenames['caddy'])