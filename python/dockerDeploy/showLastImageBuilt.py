import docker

def get_last_5_image_tags():
    try:
        # Initialize Docker client
        client = docker.from_env()

        # Get a list of all Docker images
        images = client.images.list()

        # Sort images by creation date in descending order
        images.sort(key=lambda img: img.attrs['Created'], reverse=True)

        # Extract tags of the last 5 images (if available)
        last_5_tags = []
        return images[0]

    except docker.errors.APIError as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    print("The latest image:")
    print("________________________________________________________________________")
    print("")
    print(get_last_5_image_tags())
