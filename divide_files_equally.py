import os
import shutil
import math

def delete_all_loaded_folders(folder_path):
    try:
        # List all directories in the folder
        directories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

        # Loop through the directories and delete them one by one
        for folder_name in directories:
            folder_path_to_delete = os.path.join(folder_path, folder_name)
            shutil.rmtree(folder_path_to_delete)
            print(f"Deleted folder and its contents: {folder_path_to_delete}")

        print("All loaded folders in the folder have been deleted.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Replace 'folder_path' with the path to the folder containing the subfolders you want to delete.
folder_path = "C:\\smartwatch\\dividedfiles"
delete_all_loaded_folders(folder_path)


def find_no_of_slaves_available():

    r1 = open('C:\\smartwatch\\popupresults\\windowsslave4.txt', 'r')
    r2 = open('C:\\smartwatch\\popupresults\\windowsslave3.txt', 'r')
    r3 = open('C:\\smartwatch\\popupresults\\windowsslave2.txt', 'r')


    d={}

    d['windowsslave4']=int(r1.read()); d['windowsslave3']=int(r2.read()); d['windowsslave2']=int(r3.read());

    print(d)
    l=[]
    for x in d.items():
        if 1 in x:
            l.append(x[0])
    print(l)
    print(len(l))
    return len(l), l

p, l = find_no_of_slaves_available()
print(p)
print(l)



def divide_files_into_groups(source_folder, destination_folder, num_groups):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)
    num_files = len(files)

    if num_files == 0:
        print("Source folder is empty. No files to divide.")
        return

    files_per_group = math.ceil(num_files / num_groups)

    for group_index in range(num_groups):
        start_idx = group_index * files_per_group
        end_idx = min((group_index + 1) * files_per_group, num_files)
        group_files = files[start_idx:end_idx]

        group_folder = os.path.join(destination_folder, f"group_{group_index + 1}")
        os.makedirs(group_folder, exist_ok=True)

        for file_name in group_files:
            source_file_path = os.path.join(source_folder, file_name)
            destination_file_path = os.path.join(group_folder, file_name)
            shutil.copy(source_file_path, destination_file_path)


if __name__ == "__main__":
    source_folder = "C:\\smartwatch\\randomfiles"
    destination_folder = "C:\\smartwatch\\dividedfiles"
    num_groups = len(l)

    divide_files_into_groups(source_folder, destination_folder, num_groups)
