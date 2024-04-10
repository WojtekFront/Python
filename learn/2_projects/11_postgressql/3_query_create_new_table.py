from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    print("bla bla")
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

