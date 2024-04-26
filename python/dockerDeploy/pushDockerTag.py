import docker

def push_latest_tag(image_name):
    client = docker.from_env()
    image = client.images.get(image_name)

    # List all tags of the image
    tags = image.tags

    # Find the latest tag (assuming tags are version numbers)
    latest_tag = max(tags)

    # Push the latest tag
    client.images.push(image_name)

    print(f"Successfully pushed {latest_tag} of {image_name}")

# Replace 'your_image_name' with your actual Docker image name
push_latest_tag('localhost:5000/convers:3.1.6')
