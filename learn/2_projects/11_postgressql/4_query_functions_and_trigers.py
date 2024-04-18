from conn import connect_to_db, close_connction
import random
from datetime import date


""" open connection"""
connection, cursor = connect_to_db()

new_cars_price = 1000 * random.randrange(20, 200)
cars_id = random.randrange(1, 25)

try:
    # cursor.execute("""
    # CREATE OR REPLACE FUNCTION fn_add_price(varchar, integer,integer) 
    #                RETURNS varchar --TRIGGER 
    #                AS $$
   
    #                 BEGIN
    #                     RETURN SUBSTRING($1, $2, $3);
    #                 END;
    #             $$ LANGUAGE plpgsql;
    #             """)
    cursor.execute("""
    CREATE OR REPLACE FUNCTION fn_test(word varchar, startPos integer,cnt integer) 
                   RETURNS varchar 
                    AS $$
                --   DECLARE word ALIAS for $1;
                --           startPos ALIAS for $2;
                --           cnt ALIAS for $3;
                  
   
                    BEGIN
                        RETURN SUBSTRING(word, startPos, cnt);
                    END;
                $$ LANGUAGE plpgsql;
                """)
    cursor.execute("""SELECT  * FROM fn_test('software_it',1,4)""")
    

    # cursor.execute("""CREATE TRIGGER t_update_price
    #                AFTER INSERT ON log
    #                FOR EACH ROW
    #                EXECUTE FUNCTION fn_add_price()
    #                ;""")
    cursor.execute("""
                   CREATE OR REPLACE FUNCTION fn_change_in_table()
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

    # cursor.execute("""CREATE TRIGGER t_change_table 
    #                AFTER UPDATE OR INSERT OR DELETE ON cars --, car_condition, person
    #                FOR EACH ROW
    #                EXECUTE FUNCTION fn_change_in_table();
    #             """)
    
    # cursor.execute(""" CREATE TRIGGER t_change_table_car_condition
    #                AFTER UPDATE OR INSERT OR DELETE ON car_condition
    #                FOR EACH ROW
    #                EXECUTE FUNCTION fn_change_in_table();
    #             """)
    # cursor.execute(""" CREATE TRIGGER t_change_table_person 
    #                AFTER UPDATE OR INSERT OR DELETE ON person
    #                FOR EACH ROW
    #                EXECUTE FUNCTION fn_change_in_table();
    #             """)    

except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

