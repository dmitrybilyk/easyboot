import os
import shutil
import stat

def copy_sh_files(src_directory, dest_directory):
    # Ensure the destination directory exists and is different from source
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    elif os.path.samefile(src_directory, dest_directory):
        raise ValueError("Source and destination directories are the same.")

    for filename in os.listdir(src_directory):
        if filename.endswith(".sh") or filename == os.path.basename(__file__):
            src_filepath = os.path.join(src_directory, filename)
            dest_filepath = os.path.join(dest_directory, filename)
            if os.path.isfile(src_filepath):
                shutil.copy2(src_filepath, dest_filepath)
                print(f"Copied {src_filepath} to {dest_filepath}")

def add_execution_permission(directory, extension=None):
    for filename in os.listdir(directory):
        if extension is None or filename.endswith(extension):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                st = os.stat(filepath)
                os.chmod(filepath, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
                print(f"Added execution permission to: {filepath}")

# Manually construct source directory path
home_directory = os.path.expanduser("~")
src_directory = os.path.join(home_directory, "dev", "projects", "easyboot", "docker-compose", "work", "scripts")

# Destination directory is already using os.path.expanduser("~")
dest_directory = os.path.expanduser("~")

# Call the functions
copy_sh_files(src_directory, dest_directory)
add_execution_permission(dest_directory)
