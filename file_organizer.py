import os
import shutil

def organize_files(path):
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the leading dot from the extension

        if extension:  # Check if the file has an extension
            ext_path = os.path.join(path, extension)
            file_path = os.path.join(path, file)

            if not os.path.exists(ext_path):
                os.makedirs(ext_path)
            
            shutil.move(file_path, os.path.join(ext_path, file))

if __name__ == "__main__":
    path = input("Enter path: ")
    if os.path.isdir(path):
        organize_files(path)
        print("Files organized successfully.")
    else:
        print("Invalid path. Please enter a valid directory path.")
