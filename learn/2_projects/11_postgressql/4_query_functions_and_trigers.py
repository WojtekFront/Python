from conn import connect_to_db, close_connction
import random

""" open connection"""
connection, cursor = connect_to_db()

cars_price = 1000 * random.randrange(20, 200)
cars_id = random.randrange(1, 25)

try:
    cursor.execute("""
        CREATE FUNCTION add_price(money) RETURNS integer AS $$
        DECLARE
                   quantity integer := %s;


            RETURN 
        END;
        LANGUAGE plpgsql;


    """, 
    (cars_price, cars_id))


except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

