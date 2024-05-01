import psycopg2
import subprocess
import json

def execute_db_query(query, callid, host):
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host=host,
            port="5432",
            database="eleveo_default_db"
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Execute a SQL query
        cursor.execute(query, (callid,))  # Pass callid as a parameter

        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]

        # Print column headers
        print("Column Names:", columns)

        # Fetch all the rows using fetchall() method
        rows = cursor.fetchall()

        # Display the result with column names
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Example query with callid as a parameter
query = ("SELECT cc.sid AS \"SID\", cc.direction AS \"Direction\", cc.callingagent AS \"Calling Agent\", cc.dirty AS \"Dirty\", "
         "cc.calledagent AS \"Called Agent\", cf.cftype AS \"CF Type\", cf.cfpath AS \"CF Path\" "
         # "ced.key AS \"Key\", ced.value AS \"Value\" "
         "FROM callrec.couples cc "
         "JOIN callrec.cfiles cf ON cc.id = cf.cplid "
         # "JOIN callrec.couple_extdata ced ON cc.id = ced.cplid "
         "WHERE cc.callid = %s;")

# Function to prompt user for input of a specific type
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def execute_solr_query(callId):
    try:
        # Hardcoded list of fields to filter
        hardcoded_fields_list = ['conversationId',
                                 '_version_',
                                 'eventIds',
                                 'schemaVersion',
                                 # 'correlationIds',
                                 'direction',
                                 'duration',
                                 'dayOfWeek',
                                 'secondOfDay',
                                 'startDateTime',
                                 'latestSegmentStartDateTime',
                                 'communicationTypes',
                                 # 'md_CDM_SegmentCallingAgentEleveoGroupId',
                                 # 'md_CDM_SegmentCallingAgentEmail',
                                 # 'md_CDM_SegmentCallingAgentLogin',
                                 # 'md_CDM_SegmentCallingAgentEleveoUserId',
                                 # 'labels',
                                 # 'comments',
                                 # 'contactsFrom',
                                 # 'contactsTo',
                                 # 'transcriptionUtterances',
                                 'userUUIDs',
                                 # 'groupUUIDs',
                                 # 'resourceFlags',
                                 # 'segmentsCount',
                                 # 'agentsCount',
                                 # 'interruptionCount',
                                 # 'crosstalkTime',
                                 # 'crosstalkRatio',
                                 # 'silenceCount',
                                 # 'silenceTime',
                                 # 'silenceRatio',
                                 # 'talkingCount',
                                 # 'talkingTime',
                                 # 'talkingRatio',
                                 # 'agentEmotions',
                                 # 'customerEmotion',
                                 # 'customerInterruptionCount',
                                 # 'agentInterruptionsCount'
                                 ]

        # Construct the Solr query URL with the provided conversationId
        solr_query_url = f"http://vm085.eng.cz.zoomint.com:8983/solr/conversation/query?q=correlationIds:*{callId}&indent=true&rows=1000"

        # Execute the curl command to send the Solr query and capture the output
        curl_process = subprocess.Popen(['curl', '-s', solr_query_url], stdout=subprocess.PIPE)
        query_output, _ = curl_process.communicate()

        # Decode the output from bytes to string
        query_output = query_output.decode('utf-8')

        # Parse the JSON response
        response = json.loads(query_output)

        # Extract field names and values from the response
        docs = response.get('response', {}).get('docs', [])
        formatted_output = []
        for doc in docs:
            # Filter fields based on the hardcoded list
            filtered_doc = {key: doc.get(key, None) for key in hardcoded_fields_list}
            formatted_output.append(filtered_doc)

        # Convert formatted output to JSON string
        formatted_json = json.dumps(formatted_output, indent=4)

        # Print formatted JSON output
        print("Formatted JSON output:")
        print(formatted_json)

        # Copy formatted JSON to clipboard using xclip
        subprocess.Popen(['echo', '-n', formatted_json], stdout=subprocess.PIPE).communicate()
        subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE).communicate(input=formatted_json.encode())

        # Return formatted output as JSON
        return formatted_json
    except Exception as e:
        print("An error occurred:", e)
        return None


# Prompt user for input to execute the query
vmSubIp = get_input("Enter vm IP: ", str)

if not vmSubIp:
    hostname = "vm085.eng.cz.zoomint.com"
elif len(vmSubIp) == 3:
    hostname = f"vm{vmSubIp}.eng.cz.zoomint.com"
else:
    hostname = vmSubIp

callid = get_input("Enter Call ID: ", str)
if not callid:
    callid = 138009  # Default value

# Call the function to execute the query
execute_db_query(query, callid, hostname)
response_json = execute_solr_query(callid)
if response_json:
    print("Formatted JSON output copied to clipboard.")
