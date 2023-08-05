import os
import shutil
import math

def delete_all_loaded_folders(folder_path):
    try:
        directories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

        for folder_name in directories:
            folder_path_to_delete = os.path.join(folder_path, folder_name)
            shutil.rmtree(folder_path_to_delete)
            print(f"Deleted folder and its contents: {folder_path_to_delete}")

        print("All loaded folders in the folder have been deleted.")
    except Exception as e:
        print(f"Error occurred: {e}")

folder_path = "C:\\smartwatch\\dividedfiles"
delete_all_loaded_folders(folder_path)