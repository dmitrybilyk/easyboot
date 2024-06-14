import os
import shutil

def copy_sh_files(src_directory, dest_directory):
    # Ensure the destination directory exists
    os.makedirs(dest_directory, exist_ok=True)

    # Iterate through all files in the source directory
    for filename in os.listdir(src_directory):
        if filename.endswith(".sh"):
            src_filepath = os.path.join(src_directory, filename)
            dest_filepath = os.path.join(dest_directory, filename)
            if os.path.isfile(src_filepath):
                # Copy the file to the destination directory
                shutil.copy2(src_filepath, dest_filepath)
                print(f"Copied {src_filepath} to {dest_filepath}")

# Source and destination directories
src_directory = "/home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/"
dest_directory = os.path.expanduser("~")

# Call the function
copy_sh_files(src_directory, dest_directory)
