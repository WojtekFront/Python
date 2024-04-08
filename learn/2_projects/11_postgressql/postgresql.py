import psycopg2

# open connection to database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="12345"
        )
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.OperationalError as error:
        print(f"Error connecting to database: {error}")
        exit(1)

# close connection to database
def close_connction(connnection, cursor):
    try:
        cursor.close()
        connnection.close()
    except Exception as error:
        print(f"Error closing connection to database: {error}")
        exit(1)


