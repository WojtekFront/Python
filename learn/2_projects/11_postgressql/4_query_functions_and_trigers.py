from conn import connect_to_db, close_connction
import random
from datetime import date


""" open connection"""
connection, cursor = connect_to_db()

cars_price = 1000 * random.randrange(20, 200)
cars_id = random.randrange(1, 25)

try:
    cursor.execute("""
    CREATE OR REPLACE FUNCTION fun_add_price(cars_price money) RETURNS void AS $$
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
    cursor.execute("""
                   CREATE OR REPLACE FUNCTION fun_change_in_table()
                    RETURNS TRIGGER AS $$
                    BEGIN
                        IF TG_OP = 'UPDATE' THEN
                                IF OLD IS DISTINCT FROM NEW THEN
                                    INSERT INTO log (planned_maintance, type, description) 
                                    VALUES ('2024-04-15','update','new');
                                END IF;
                            RETURN NEW;
                        ELSIF TG_OP = 'INSERT' THEN
                                INSERT INTO log (planned_maintance, type, description) 
                                VALUES ('2024-04-15','insert','new');
                            RETURN NEW;                        
                        ELSIF TG_OP = 'DELETE' THEN
                                INSERT INTO log (planned_maintance, type, description) 
                                VALUES ('2024-04-15','delete','new');
                            RETURN OLD;
                        END IF;
                    END;
                   $$ LANGUAGE plpgsql;
                   ;""")

    cursor.execute("""CREATE TRIGGER t_change_table 
                   AFTER UPDATE OR INSERT OR DELETE ON cars, car_condition, person
                   FOR EACH ROW
                   EXECUTE FUNCTION fun_change_in_table();
                   
                """)

except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

