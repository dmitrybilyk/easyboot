import subprocess

def remove_unused_images():
    try:
        # Command to list images with "none" tag
        cmd_list_images = "docker image ls | grep integrations"

        # Run the command to get image IDs
        result = subprocess.run(cmd_list_images, shell=True, capture_output=True, text=True)
        image_ids = result.stdout.strip().split()  # Split output into a list of image IDs

        if image_ids:
            # Command to remove images by IDs
            cmd_remove_images = f"docker image rm {' '.join(image_ids)} -f"

            # Run the command to remove images
            subprocess.run(cmd_remove_images, shell=True, check=True)
            print("Unused Docker images removed successfully.")
        else:
            print("No unused Docker images found.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Handle error if the subprocess command fails

# Call the function to remove unused Docker images
remove_unused_images()
