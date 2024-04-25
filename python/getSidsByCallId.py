import psycopg2

def execute_query(query, callid):
    try:
        # Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="vm085.eng.cz.zoomint.com",
            port="5432",
            database="eleveo_default_db"
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Execute a SQL query
        cursor.execute(query, (callid,))  # Pass callid as a parameter

        # Fetch all the rows using fetchall() method
        rows = cursor.fetchall()

        # Display the result
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Example query with callid as a parameter
query = ("SELECT cc.sid AS \"SID\", cc.direction AS \"Direction\", cc.callingagent AS \"Calling Agent\", cc.dirty AS \"Dirty\", "
         "cc.calledagent AS \"Called Agent\", cf.cftype AS \"CF Type\", cf.cfpath AS \"CF Path\" "
         "FROM callrec.couples cc JOIN callrec.cfiles cf ON cc.id = cf.cplid WHERE cc.callid = %s;")

# Example callid
callid = 138009

# Call the function to execute the query
execute_query(query, callid)
