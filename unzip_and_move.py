from constants import *
import zipfile
import os


directory = DATA_DUMP_FOLDER
# List all files in the directory
files = os.listdir(directory)
# Filter out only files (not directories)
files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

zip_filenames = {}
# Print the list of files
for file in files:
    if "caddy" in file:
        zip_filenames["caddy"] = file
    elif "erico" in file:
        zip_filenames["erico"] = file
    elif "eriflex" in file:
        zip_filenames["eriflex"] = file


'''
This function should copy the zip folder from the original dump area to the archive folder and clear all files in the temp folder
'''
def archive_and_clear_temp(whichfile: str):
    old_path_to_zip = DATA_DUMP_FOLDER + '\\' + zip_filenames[whichfile]
    new_path_to_zip = DATA_ARCHIVE_FOLDER + '\\' + zip_filenames[whichfile]
    # try to move the file and catch any errors
    try:
        print(f"trying to move {old_path_to_zip} to {new_path_to_zip}...")
        os.rename(old_path_to_zip, new_path_to_zip)
        print(f"{GREEN}{old_path_to_zip} has been moved to {new_path_to_zip} successfully{RESET}")
    except FileNotFoundError:
        print(f"{RED}{old_path_to_zip} not found.{RESET}")
    except FileExistsError:
        print(f"{RED}{new_path_to_zip} already exists.{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred: {RED}{e}")
        print()

    print(f"removing files from {TEMP_DATA_FOLDER}...")
    # iterate over all files in the path and remove them
    for filename in os.listdir(TEMP_DATA_FOLDER):
        filepath = os.path.join(TEMP_DATA_FOLDER, filename)
        try:
            print(f"trying to remove {filepath}...")
            os.remove(filepath)
            print(f"{GREEN}{filepath} removed successfully.{RESET}")
        except FileNotFoundError:
            print(f"{RED}{filepath} not found.{RESET}")
        except Exception as e:
            print(f"{RED}An error occurred: {RESET}{e}")
            print()

'''
This function should unzip the contents of the zip in the dump folder to the temp folder
Whichfile is a string that is a key in the zip_filenames dictionary
'''
def unzip_to_temp(whichfile: str):
    
    path_to_zip = DATA_DUMP_FOLDER + '\\' + zip_filenames[whichfile]
    
    try:
        #unzip the file
        with zipfile.ZipFile(path_to_zip) as f:
            print(f"Extracting Files for {whichfile}...")
            f.extractall(TEMP_DATA_FOLDER)
        print(f"{GREEN}Files extracted successfully.{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred.{RESET}{e}")
    