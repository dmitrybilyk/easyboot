import os
import shutil
import stat

def copy_sh_files(src_directory, dest_directory):
    # Ensure the destination directory exists
    os.makedirs(dest_directory, exist_ok=True)

    # Iterate through all files in the source directory
    for filename in os.listdir(src_directory):
        if filename.endswith(".sh") or filename == os.path.basename(__file__):
            src_filepath = os.path.join(src_directory, filename)
            dest_filepath = os.path.join(dest_directory, filename)
            if os.path.isfile(src_filepath):
                # Copy the file to the destination directory
                shutil.copy2(src_filepath, dest_filepath)
                print(f"Copied {src_filepath} to {dest_filepath}")

def add_execution_permission(directory, extension=None):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if extension is None or filename.endswith(extension):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # Get the current permissions of the file
                st = os.stat(filepath)
                # Add execution permissions for the user, group, and others
                os.chmod(filepath, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
                print(f"Added execution permission to: {filepath}")

# Source and destination directories
src_directory = "/home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/"
dest_directory = os.path.expanduser("~")

# Call the function
copy_sh_files(src_directory, dest_directory)
add_execution_permission(dest_directory)

