from conn import connect_to_db, close_connction
import random

""" open connection"""
connection, cursor = connect_to_db()

cars_price = 1000 * random.randrange(20, 200)
cars_id = random.randrange(1, 25)

try:
    cursor.execute("""
    CREATE OR REPLACE FUNCTION add_price(cars_price money) RETURNS void AS $$
    DECLARE
        cars_id integer;
    BEGIN
        -- Random select cars_id
        cars_id := trunc(random() * 24 + 1)::integer;

        -- Actualization cars_price for random cars_id
        UPDATE cars
        SET price = cars_price
        WHERE id = cars_id;
    END;
    $$ LANGUAGE plpgsql;
    """)


except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

