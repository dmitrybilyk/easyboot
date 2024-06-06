import pysolr
import sys

# Specify the Solr server URL
solr_url = 'http://localhost:8983/solr/conversation'

# Create a connection to Solr
solr = pysolr.Solr(solr_url, always_commit=True)

def find_and_remove_field(conversation_id, field_name):
    # Build a query to find the conversation by conversationId
    query = f"conversationId:{conversation_id}"

    # Perform a search to find the conversation document
    results = solr.search(query)

    # Check if any documents were found
    if results.hits > 0:
        # Assuming there's only one document (unique conversationId)
        conversation_doc = results.docs[0]
        doc_id = conversation_doc['conversationId']

        # Debug: Print document keys and structure
        print(f"Found document keys: {conversation_doc.keys()}")

        # Check if the specified field exists in the document
        if field_name in conversation_doc:
            # Create a copy of the conversation document
            updated_doc = conversation_doc.copy()

            # Remove the specified field from the copied document
            del updated_doc[field_name]

            # Debug: Print updated document before sending to Solr
            print(f"Updated document: {updated_doc}")

            # Update the document in Solr without the specified field
            solr.add([updated_doc])

            print(f"Updated conversation with conversationId {conversation_id}. Removed field {field_name}")
        else:
            print(f"Field {field_name} not found in conversation with conversationId {conversation_id}")
    else:
        print(f"Conversation with conversationId {conversation_id} not found")

# Example usage:
if __name__ == "__main__":
    conversation_id = "6c09ca35-896d-46e1-a39a-f8eeced2347d"

    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 1:
        conversation_id = sys.argv[1]


    field_name = "autoReviewRuleIds"  # Field to be removed

    # Call the function to find and remove the field from the conversation document
    find_and_remove_field(conversation_id, field_name)
