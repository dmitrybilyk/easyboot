import pika
import json

# Connection parameters
credentials = pika.PlainCredentials('callrec', 'callrec')  # default credentials
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

# Establish connection
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Queue declaration (ensure queue exists before pushing)
channel.queue_declare(queue='my_queue', durable=True)  # durable=True makes the queue persistent

# JSON object to push into the queue
json_object = {
    "tenantId": "default",
    "sid": "17841350192.168.99.206:20036192.168.99.220:18628_1_2",
    "attemptsCount": 1,
    "speechPhraseOccurrences":
        [
            {
                "id": 9,
                "from": "2015-05-12T13:54:27Z",
                "to": "2015-05-12T13:54:28Z",
                "speechPhrase": {
                    "id": 64,
                    "phrase": "Really frustrating"
                },
                "speechTag": [
                    {
                    "id": 7,
                    "name": "Customer Dissatisfaction",
                    "icon": "sign_stop"
                }
                ],
                "confidence": 0.9900000095367432,
                "channel": "LEFT"
            }
        ]
}

# Convert JSON object to string
json_string = json.dumps(json_object)

# Push JSON string into the queue
channel.basic_publish(exchange='', routing_key='encourage-zqm-connector-speechphrase-consumer', body=json_string,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print("JSON object sent to the queue")

# Close connection
connection.close()