import psycopg2
from psycopg2 import Error

# PostgreSQL connection parameters
db_host = 'localhost'
db_name = 'eleveo_default_db'
db_user = 'postgres'
db_password = 'postgres'

# SQL query to execute
sql_query = "SELECT COUNT(*) FROM callrec.couples;"

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object using the cursor() method
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch the result
    count = cursor.fetchone()[0]
    print(f"Number of rows in callrec.couples: {count}")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Closing database connection.
    if connection:
        cursor.close()
        connection.close()
