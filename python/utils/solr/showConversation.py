import pysolr

# Specify the Solr server URL
solr_url = 'http://localhost:8983/solr/conversation'

# Create a connection to Solr
solr = pysolr.Solr(solr_url, always_commit=True)  # always_commit=True automatically commits after each operation

def search_documents(query):
    # Perform a search query
    results = solr.search(query)

    # Print the total number of results found
    print(f"Total documents found: {results.hits}")

    # Print each document's fields
    for result in results:
        print(f"ConversationId ID: {result['conversationId']}")
        print(f"Document Fields: {result}")

# Example usage:
if __name__ == "__main__":
    query = "conversationId:faead484-eca5-4a6e-a0e7-19428c634133"
    search_documents(query)
