from datetime import timedelta, datetime
import constants
import zipfile
import os

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

zip_filenames = {
    "caddy": yesterday + "-catalogdata-caddy.zip",
    "erico": yesterday + "-catalogdata-erico.zip",
}

'''
This function should copy the zip folder from the original dump area to the archive folder and clear all files in the temp folder
'''
def archive_and_clear_temp(whichfile: str):
    old_path_to_zip = constants.DATA_DUMP_FOLDER + '\\' + zip_filenames[whichfile]
    new_path_to_zip = constants.DATA_ARCHIVE_FOLDER + '\\' + zip_filenames[whichfile]
    # try to move the file and catch any errors
    try:
        os.rename(old_path_to_zip, new_path_to_zip)
    except FileNotFoundError:
        print(f"{old_path_to_zip} not found.")
    except FileExistsError:
        print(f"{new_path_to_zip} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    for filename in os.listdir(constants.TEMP_DATA_FOLDER):
        file_path = os.path.join(constants.TEMP_DATA_FOLDER, filename)
        print(file_path)


'''
This function should unzip the contents of the zip in the dump folder to the temp folder
Whichfile is a string that is a key in the zip_filenames dictionary
'''
def unzip_to_temp(whichfile: str):
    
    path_to_zip = constants.DATA_DUMP_FOLDER + '\\' + zip_filenames[whichfile]
    
    #unzip the file
    with zipfile.ZipFile(path_to_zip) as f:
        print(f"Extracting Files for {whichfile}...")
        f.extractall(constants.TEMP_DATA_FOLDER)
    

unzip_to_temp('caddy')
archive_and_clear_temp('caddy')
#print(path_to_zip + '\\' + zip_filenames['caddy'])