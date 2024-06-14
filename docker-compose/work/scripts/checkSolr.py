import requests

# Solr URL and collection name
solr_url = 'http://localhost:8983/solr/'
collection_name = 'conversation'

# Query to get number of documents
query_docs = f'{solr_url}{collection_name}/select?q=*:*&rows=0'

# Query to search for documents with eventIds containing 'voicetagid'
query_eventids = f'{solr_url}{collection_name}/select?q=eventIds:*voicetagid*&rows=10'

try:
    # Sending the query to Solr to get number of documents
    response_docs = requests.get(query_docs)

    # Sending the query to Solr to search for documents with eventIds containing 'voicetagid'
    response_eventids = requests.get(query_eventids)

    # Initialize variables
    num_docs = -1
    num_docs_with_voicetagid = 0

    # Checking if the request for number of documents was successful
    if response_docs.status_code == 200:
        num_docs = response_docs.json()['response']['numFound']
    else:
        print(f"Failed to retrieve number of documents from Solr. Status code: {response_docs.status_code}")

    # Checking if the request for eventIds containing 'voicetagid' was successful
    if response_eventids.status_code == 200:
        num_docs_with_voicetagid = response_eventids.json()['response']['numFound']
    else:
        print(f"Failed to retrieve documents with 'voicetagid' from Solr. Status code: {response_eventids.status_code}")

    # Displaying results
    print(f"Number of documents in collection: {num_docs}")
    print(f"Number of documents with 'voicetagid' in eventIds: {num_docs_with_voicetagid}")

    # Check if the collection is empty
    if num_docs == 0:
        print("Solr collection is empty.")

except requests.exceptions.RequestException as e:
    print(f"Error connecting to Solr: {e}")
