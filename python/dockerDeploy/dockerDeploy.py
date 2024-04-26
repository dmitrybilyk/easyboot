import docker

def find_latest_image():
    try:
        client = docker.from_env()
        images = client.images.list()

        # Sort images by creation date to get the latest one
        images.sort(key=lambda img: img.attrs['Created'], reverse=True)

        if images:
            latest_image = images[0]
            return latest_image
        else:
            return None

    except docker.errors.APIError as e:
        print(f"Error: {e}")
        return None

def tag_latest_image_with_new_tag(image, newTag):
    try:
        if image:
            new_tag = f"localhost:5000/{newTag}"
            # Tag the latest image with the new tag
            image.tag(new_tag)
            return new_tag
        else:
            return None

    except docker.errors.APIError as e:
        print(f"Error tagging image: {e}")
        return None

if __name__ == "__main__":
    latest_image = find_latest_image()

    if latest_image:
        newTag = 'convers:3.1.2'
        new_tag = tag_latest_image_with_new_tag(latest_image, newTag)

        if new_tag:
            print(f"Successfully tagged the latest image with: {new_tag}")
        else:
            print("Failed to tag the latest image.")
    else:
        print("No images found.")
