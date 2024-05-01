import pika
import requests

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 15672  # Default port for RabbitMQ Management API
username = 'callrec'
password = 'callrec'

# Get list of queues from RabbitMQ Management API
def get_queues():
    management_api_url = f'http://{rabbitmq_host}:{rabbitmq_port}/api/queues'
    response = requests.get(management_api_url, auth=(username, password))
    if response.status_code == 200:
        queues = [queue['name'] for queue in response.json()]
        return queues
    else:
        print(f"Failed to retrieve queues. Status code: {response.status_code}")
        return []

# Print list of queues
print("List of queues on RabbitMQ server:")
queues = get_queues()
for queue in queues:
    print(queue)
