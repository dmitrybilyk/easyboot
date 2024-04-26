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
        for image in images[:5]:
            tags = image.tags
            if tags:
                last_5_tags.extend(tags)

        return last_5_tags

    except docker.errors.APIError as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    last_5_tags = get_last_5_image_tags()

    if last_5_tags:
        print("Last 5 Docker image tags:")
        for tag in last_5_tags:
            print(tag)
    else:
        print("No Docker images found or failed to retrieve tags.")
