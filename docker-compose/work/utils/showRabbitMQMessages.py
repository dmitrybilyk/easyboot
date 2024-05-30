import pika
import json
import subprocess
import requests
import sys

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
queue_name = 'conversations-to-save'
username = 'callrec'
password = 'callrec'

# Establish connection
credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
channel = connection.channel()

def get_queues():
    management_api_url = f'http://{rabbitmq_host}:{rabbitmq_port}/api/queues'
    response = requests.get(management_api_url, auth=(username, password))
    if response.status_code == 200:
        queues = [queue['name'] for queue in response.json()]
        return queues
    else:
        print(f"Failed to retrieve queues. Status code: {response.status_code}")
        return []


try:

    # Function to fetch messages from the queue without consuming
    def fetch_messages():
        messages = []

        # queues = get_queues()
        print(queue_name)
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
        while method_frame:
            message = body.decode('utf-8')
            try:
                message_data = json.loads(message)  # Attempt to parse message as JSON
                messages.append(message_data)
            except json.JSONDecodeError as e:
                print(f"Ignoring invalid JSON message: {message}")
                # Optionally handle or log the JSON decode error
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
        return messages

    # Fetch messages from the queue without consuming
    print("Fetching messages from the queue without consuming...")
    messages = fetch_messages()

    # Print messages
    print("Messages read from the queue:")
    for message in messages:
        print(message)

    # Convert messages list to JSON string
    json_output = json.dumps(messages, indent=4)

    # Print formatted JSON content
    print("Formatted JSON content:")
    print(json_output)

    # Copy formatted JSON content to clipboard using xclip
    proc = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    proc.communicate(input=json_output.encode())

    print("JSON content copied to clipboard")

finally:
    # Close connection
    connection.close()

def main():
    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 1:
        # The first command-line argument (sys.argv[0]) is the script name
        # Subsequent arguments are the values passed
        queue_name = sys.argv[1:]

if __name__ == "__main__":
    main()
