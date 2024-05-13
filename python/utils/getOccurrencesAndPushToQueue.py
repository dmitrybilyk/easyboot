import psycopg2
import json

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="eleveo_default_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Define your new SQL query
sql_query = """
select soc.*, sp.id, sp.phrase, ttp.tag_id, ttp.phrase_id
from speechrec_core.speech_phrase_occurrences soc
    join speechrec_core.speech_phrases sp on
        soc.phrase_id = sp.id
    join speechrec_core.tags_to_phrases ttp on
        sp.id = ttp.phrase_id
where sid = '17841350192.168.99.206:20036192.168.99.220:18628_1_2';
"""

# Define your new SQL query
sql_query_for_tags = """
select soc.*, sp.id, sp.phrase, ttp.tag_id, ttp.phrase_id,
       st.id as tag_id, st.name as tag_name, st.icon as tag_icon
from speechrec_core.speech_phrase_occurrences soc
         join speechrec_core.speech_phrases sp on
    soc.phrase_id = sp.id
         join speechrec_core.tags_to_phrases ttp on
    sp.id = ttp.phrase_id
        join speechrec_core.speech_tags st on
    ttp.tag_id = st.id
where sid = '5248412010.107.86.62:1924410.107.80.115:31262_4';
"""


# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the new SQL query
cursor.execute(sql_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
conn.close()

# Convert the query result to a structured JSON object
result_dict = {}
for row in rows:
    formatted_row = list(row)  # Convert tuple to list to modify elements

    # Extract main attributes from the row
    result_id = formatted_row[0]
    sid = formatted_row[1]
    phrase_id = formatted_row[2]
    from_timestamp = formatted_row[3].strftime("%Y-%m-%dT%H:%M:%SZ")
    to_timestamp = formatted_row[4].strftime("%Y-%m-%dT%H:%M:%SZ")
    confidence = formatted_row[5]
    channel = formatted_row[6]
    phrase = formatted_row[7]
    tag_id = formatted_row[8]
    tag_phrase_id = formatted_row[9]

    # Create a new entry in result_dict if it doesn't exist yet
    if result_id not in result_dict:
        result_dict[result_id] = {
            "id": result_id,
            "sid": sid,
            "phrase_id": phrase_id,
            "from_timestamp": from_timestamp,
            "to_timestamp": to_timestamp,
            "confidence": confidence,
            "channel": channel,
            "speechPhrase": {
                "phrase_id": phrase_id,
                "phrase": phrase,
                "tags": []  # Initialize empty list for tags
            }
        }

# Convert the dictionary values (results) into a list
result_list = list(result_dict.values())

# Convert the list of dictionaries to a JSON object
result_json = json.dumps(result_list, indent=4)

# Print the JSON object (optional)
print(result_json)

