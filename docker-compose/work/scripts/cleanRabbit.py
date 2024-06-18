import requests
import logging
from requests.auth import HTTPBasicAuth

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_queue_names(rabbitmq_api_url, auth):
    response = requests.get(f'{rabbitmq_api_url}/queues', auth=auth)
    if response.status_code == 200:
        queues = response.json()
        return [queue['name'] for queue in queues]
    else:
        logging.error(f"Failed to retrieve queues: {response.status_code} {response.text}")
        return []

def purge_queue(rabbitmq_api_url, queue_name, auth):
    response = requests.delete(f'{rabbitmq_api_url}/queues/%2F/{queue_name}/contents', auth=auth)
    if response.status_code == 204:
        logging.info(f"Purged queue: {queue_name}")
    else:
        logging.error(f"Failed to purge queue {queue_name}: {response.status_code} {response.text}")

def purge_all_queues(rabbitmq_api_url, auth):
    queue_list = get_queue_names(rabbitmq_api_url, auth)
    logging.info(f"Found queues: {queue_list}")

    for queue_name in queue_list:
        purge_queue(rabbitmq_api_url, queue_name, auth)

    logging.info("All queues purged successfully.")

if __name__ == '__main__':
    # RabbitMQ Management API details
    rabbitmq_api_url = 'http://localhost:15672/api'
    username = 'callrec'
    password = 'callrec'

    auth = HTTPBasicAuth(username, password)

    purge_all_queues(rabbitmq_api_url, auth)
