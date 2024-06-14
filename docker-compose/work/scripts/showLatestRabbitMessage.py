import pika
import json
import pyperclip
import requests
import sys

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
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

# Function to fetch the latest message from a specific queue
def fetch_latest_message(queue_name):
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=False)
    if method_frame:
        message = body.decode('utf-8')
        try:
            message_data = json.loads(message)
            return message_data
        except json.JSONDecodeError as e:
            print(f"Ignoring invalid JSON message: {message}")
            return None
    else:
        print(f"No message found in queue '{queue_name}'")
        return None

def main():
    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 1:
        queue_name = sys.argv[1]
    else:
        print("Usage: python script_name.py <queue_name>")
        sys.exit(1)  # Exit the script if no queue name is provided

    try:
        # Fetch latest message from the specified queue
        print(f"Fetching latest message from queue '{queue_name}'...")
        latest_message = fetch_latest_message(queue_name)

        if latest_message:
            # Print the latest message
            print("Latest message:")
            print(json.dumps(latest_message, indent=4))

            # Copy to clipboard using pyperclip
            json_output = json.dumps(latest_message, indent=4)
            pyperclip.copy(json_output)

            print("JSON content copied to clipboard")
        else:
            print(f"No valid message retrieved from queue '{queue_name}'")

    finally:
        # Close connection
        connection.close()

if __name__ == "__main__":
    main()
