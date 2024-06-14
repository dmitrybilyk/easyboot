import os
import stat

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

# Get the home directory
home_directory = os.path.expanduser("~")

# Call the function to add execution permission to all files in the home directory
# add_execution_permission(home_directory)

# If you want to target only specific file types, e.g., .sh files, use:
add_execution_permission(home_directory, ".sh")
