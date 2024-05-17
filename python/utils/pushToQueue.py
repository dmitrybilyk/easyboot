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
    "sid": "19885689192.168.10.134:24590192.168.10.179:24576_137022",
    "attemptsCount": 1,
    "speechPhraseOccurrences":
        [
            {
                "id": 79,
                "from": "2024-05-02T03:28:03Z",
                "to": "2024-05-02T03:28:04Z",
                "speechPhrase": {
                    "id": 193,
                    "phrase": "Can we go ahead"
                },
                "speechTag": [
                    {
                    "id": 22,
                    "name": "Sales Close",
                    "icon": "pin_green"
                }
                ],
                "confidence": 0.5099999904632568,
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