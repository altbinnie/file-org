import os
import shutil

def organize_files(src_folder, dest_folder):
    # does the destination folder exists?
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    # make a list of the files in the folder
    files = os.listdir(src_folder)
    for file in files:
        # Ignore directories
        if os.path.isdir(os.path.join(src_folder, file)):
            continue
        # file extension
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()
        # Create a new folder to file type
        type_folder = os.path.join(dest_folder, file_extension[1:])
        if not os.path.exists(type_folder):
            os.makedirs(type_folder)
        # set the file to the folder
        shutil.move(os.path.join(src_folder, file), os.path.join(type_folder, file))
    print("Organizacao completa")

# teste
src_directory = "C:\\Users\\User\\documents\\EXAMPLE"
# i want the folders to be in the same directories, so:
dest_directory = src_directory

organize_files(src_directory, dest_directory)
