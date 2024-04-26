import subprocess
import json

conversation_id = "e86bd021-7971-40c9-bcb4-4ceca7027fdf"  # Example conversationId

def execute_solr_query(conversation_id):
    try:
        # Hardcoded list of fields to filter
        hardcoded_fields_list = ['conversationId',
                                 '_version_',
                                 'eventIds',
                                 # 'schemaVersion',
                                 # 'correlationIds',
                                 # 'direction',
                                 # 'duration',
                                 # 'dayOfWeek',
                                 # 'secondOfDay',
                                 # 'startDateTime',
                                 # 'latestSegmentStartDateTime',
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
        solr_query_url = f"http://vm085.eng.cz.zoomint.com:8983/solr/conversation/query?q=conversationId:{conversation_id}&indent=true&rows=1000"

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

# Example usage:
response_json = execute_solr_query(conversation_id)
if response_json:
    print("Formatted JSON output copied to clipboard.")
