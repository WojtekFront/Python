from conn import connect_to_db, close_connction
from datetime import date

today_date   =  date.today() 
""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS log(
                   id SERIAL PRIMARY KEY,
                   planned_maintenance DATE NOT NULL,
                   type VARCHAR(50),
                   description VARCHAR(200)
                   );""")
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

