from conn import connect_to_db, close_connction
import random

connection, cursor = connect_to_db()

price = random.randrange(10000, 100000)

try:
    cursor.execute("""
                WITH selected_row AS (
                   SELECT id
                   FROM cars
                   WHERE price_gross::numeric = 0
                   LIMIT 1
                )
                INSERT INTO cars (price_gross, color) 
                SELECT %s , 'default_color'
                FROM selected_row
                RETURNING id, price_gross
                ;""",(price,))

    insert_row = cursor.fetchone()
    print(insert_row)

   
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

