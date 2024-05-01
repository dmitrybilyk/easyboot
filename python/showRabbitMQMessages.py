import pika

# Function to prompt user for input of a specific type
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = '5672'
queue_name = 'speechrec-segments-to-analyze'
username = 'callrec'
password = 'callrec'

# Establish connection
credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=queue_name, durable=True)

# Function to fetch last three messages
def fetch_last_three_messages():
    messages = []
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
    while method_frame:
        messages.append(body.decode('utf-8'))
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

    # Return last three messages
    return messages[-3:]

# Fetch and print last three messages
last_three_messages = fetch_last_three_messages()
print("Last Three Messages:")
for message in last_three_messages:
    print(message)

# Close connection
connection.close()