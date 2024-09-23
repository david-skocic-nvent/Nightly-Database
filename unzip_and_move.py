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
        print(f"trying to move {old_path_to_zip} to {new_path_to_zip}...")
        os.rename(old_path_to_zip, new_path_to_zip)
        print(f"{old_path_to_zip} has been moved to {new_path_to_zip} successfully.")
    except FileNotFoundError:
        print(f"{old_path_to_zip} not found.")
    except FileExistsError:
        print(f"{new_path_to_zip} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"removing files from {constants.TEMP_DATA_FOLDER}...")
    # iterate over all files in the path and remove them
    for filename in os.listdir(constants.TEMP_DATA_FOLDER):
        filepath = os.path.join(constants.TEMP_DATA_FOLDER, filename)
        try:
            print(f"trying to remove {filepath}...")
            os.remove(filepath)
            print(f"{filepath} removed successfully.")
        except FileNotFoundError:
            print(f"{filepath} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


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
    