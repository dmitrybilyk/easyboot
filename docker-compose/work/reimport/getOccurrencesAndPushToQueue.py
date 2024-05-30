import psycopg2
import json
import pika

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="eleveo_default_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Define your main SQL query to retrieve speech phrase occurrences
sql_query = """
SELECT soc.*, sp.id, sp.phrase, ttp.tag_id, ttp.phrase_id
FROM speechrec_core.speech_phrase_occurrences soc
JOIN speechrec_core.speech_phrases sp ON soc.phrase_id = sp.id
JOIN speechrec_core.tags_to_phrases ttp ON sp.id = ttp.phrase_id
"""

# Define your SQL query to retrieve tags for a specific phrase_id
sql_query_for_tags = """
SELECT st.id AS tag_id, st.name AS tag_name, st.icon AS tag_icon
FROM speechrec_core.speech_tags st
JOIN speechrec_core.tags_to_phrases ttp ON st.id = ttp.tag_id
WHERE ttp.phrase_id = %s;
"""

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the main SQL query
cursor.execute(sql_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Convert the query result to a structured JSON object
speech_phrase_occurrences = []
for row in rows:
    formatted_row = list(row)  # Convert tuple to list to modify elements

    # Extract main attributes from the row
    sid = formatted_row[1]
    result_id = formatted_row[0]
    phrase_id = formatted_row[2]
    from_timestamp = formatted_row[3].strftime("%Y-%m-%dT%H:%M:%SZ")
    to_timestamp = formatted_row[4].strftime("%Y-%m-%dT%H:%M:%SZ")
    confidence = formatted_row[5]
    channel = formatted_row[6]
    phrase = formatted_row[7]
    tag_id = formatted_row[8]
    tag_phrase_id = formatted_row[9]

    # Execute the SQL query for tags for each phrase_id
    cursor.execute(sql_query_for_tags, (phrase_id,))
    tag_rows = cursor.fetchall()
    tags = []

    for tag_row in tag_rows:
        tag_id = tag_row[0]
        tag_name = tag_row[1]
        tag_icon = tag_row[2]
        tags.append({
            "id": tag_id,
            "name": tag_name,
            "icon": tag_icon
        })

    # Create speech phrase occurrence object
    speech_phrase_occurrence = {
        "tenantId": "default",
        "sid": sid,
        "attemptsCount": 1,
        "speechPhraseOccurrences": [{
            "id": result_id,
            "phrase_id": phrase_id,
            "from": from_timestamp,
            "to": to_timestamp,
            "confidence": confidence,
            "channel": channel,
            "speechPhrase": {
                "id": phrase_id,
                "phrase": phrase,
            },
            "speechTag": tags  # Changed to a list to accommodate multiple tags
        }]
    }
    speech_phrase_occurrences.append(speech_phrase_occurrence)

# Close the cursor and database connection
cursor.close()
conn.close()

# Establish connection to RabbitMQ server
credentials = pika.PlainCredentials('callrec', 'callrec')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Queue declaration
channel.queue_declare(queue='my_queue', durable=True)

# Push each speech phrase occurrence object to the queue separately
for speech_occurrence in speech_phrase_occurrences:
    # Convert the speech phrase occurrence object to a JSON string
    result_json = json.dumps(speech_occurrence, indent=4)

    # Push JSON string into the queue
    channel.basic_publish(
        exchange='',
        routing_key='encourage-zqm-connector-speechphrase-consumer',
        body=result_json,
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        )
    )
    print("JSON object sent to the queue:", result_json)

# Close the connection
connection.close()
