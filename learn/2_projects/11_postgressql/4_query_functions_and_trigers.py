from conn import connect_to_db, close_connction
import random
from datetime import date

""" open connection"""
connection, cursor = connect_to_db()

new_cars_price = 1000 * random.randrange(20, 200)
cars_id = random.randrange(1, 25)

try:
    # cursor.execute(""" DROP FUNCTION IF EXISTS fn_add_price() CASCADE;""")
    # cursor.execute("""
    # CREATE OR REPLACE FUNCTION fn_add_price() 
    #                RETURNS void --TRIGGER 
    #                AS $$
   
    #                 BEGIN
    #                    INSERT INTO log ( type, description) VALUES( 'change', 'new2');
    #                 END;
    #             $$ LANGUAGE plpgsql;
    #             """)
    # cursor.execute(""" DROP ROUTINE IF EXISTS fn_add_price(int, int) CASCADE;""")
  
    # cursor.execute("""
    #                CREATE OR REPLACE FUNCTION fn_add_price(int, int)
    #                RETURNS int
    #                AS 
    #                $body$
    #                -- INSERT INTO log
    #                --BEGIN
    #                SELECT $1 + $2 + $1;
    #                --END;
    #                $body$
    #                LANGUAGE SQL -- Using the SQL language                
    #                """)

    # cursor.execute("""
    #           CREATE OR REPLACE FUNCTION fn_test(word varchar, startPos integer,cnt integer) 
    #                RETURNS varchar 
    #                 AS $$
    #             --   DECLARE word ALIAS for $1;
    #             --           startPos ALIAS for $2;
    #             --           cnt ALIAS for $3;
    #                 BEGIN
    #                     RETURN SUBSTRING(word, startPos, cnt);
    #                 END;
    #             $$ LANGUAGE plpgsql;
    #             """)

    # cursor.execute("""SELECT  * FROM fn_test('software_it',1,4)""")
    # cursor.execute("""
    #             CREATE OR REPLACE FUNCTION fn_test2(first_word varchar, second_word varchar) 
    #                RETURNS varchar 
    #                 AS $$
    #                 BEGIN
    #                     IF first_word IS null OR second_word IS null THEN
    #                         RETURN 'First word or second word is null';
    #                     ELSE
    #                     --    RETURN first_word ||' ' || second_word;
    #                           RETURN concat_ws(' / ', initCap(first_word), initCap(first_word));
    #                     END IF;
    #                 END;
    #             $$ LANGUAGE plpgsql;
    #             """)

    # cursor.execute("""SELECT  * FROM fn_test2('software', 'IT');""")
    # cursor.execute(""" CREATE OR REPLACE FUNCTION fn_test3(inout num1 int, inout num2 int)
    #                AS $$
    #                BEGIN
    #                     SELECT num1, num2 INTO num2, num1;
    #                END;
    #                $$
    #                LANGUAGE plpgsql;
    #                ;""")

    # cursor.execute("""SELECT * FROM fn_test3(11, 22)""")
    # cursor.execute(""" CREATE OR REPLACE FUNCTION fn_test4(numeric[])
    #                returns numeric
    #                AS $$
    #                DECLARE total numeric :=0;
    #                        val numeric;
    #                        cnt int := 0;
    #                        n_array ALIAS for $1;
    #                BEGIN
    #                     foreach val in array n_array
    #                     LOOP
    #                         total := total + val;
    #                         cnt := cnt + 1;
    #                     END LOOP;
    #                     RETURN total/cnt;
    #                END;
    #                $$
    #                LANGUAGE plpgsql
    #                ;""")
    
    # cursor.execute("""SELECT fn_test4(array[1,2,3,4,5])""")

    # cursor.execute("""CREATE TRIGGER t_update_price
    #                AFTER INSERT ON log
    #                FOR EACH ROW
    #                EXECUTE FUNCTION fn_add_price()
    #                ;""")

    cursor.execute(""" DROP FUNCTION IF EXISTS fn_change_in_table() CASCADE ;""")
    cursor.execute("""
                   CREATE OR REPLACE FUNCTION fn_change_in_table()
                    RETURNS TRIGGER AS $$
                    BEGIN
                        IF TG_OP = 'UPDATE' THEN
                                IF OLD IS DISTINCT FROM NEW THEN
                                    INSERT INTO log (planned_maintenance, type, description) 
                                    VALUES (CURRENT_DATE,'update','new2');
                                END IF;
                            RETURN NEW;
                        ELSIF TG_OP = 'INSERT' THEN
                                INSERT INTO log (planned_maintenance, type, description) 
                                VALUES (CURRENT_DATE,'insert','new1');
                            RETURN NEW;                        
                        ELSIF TG_OP = 'DELETE' THEN
                                INSERT INTO log (planned_maintenance, type, description) 
                                VALUES (CURRENT_DATE,'delete','new1');
                            RETURN OLD;
                        END IF;
                    END;
                   $$ LANGUAGE plpgsql;
                   """)    

    # cursor.execute("""
    #                SELECT MAX(price_gross::NUMERIC) FROM cars;
    #                """)

    # cursor.execute("""
    #                CREATE OR REPLACE FUNCTION fn_change_in_table()
    #                 RETURNS TRIGGER AS $$
    #                 BEGIN
    #                     IF TG_OP = 'UPDATE' THEN
    #                             IF OLD IS DISTINCT FROM NEW THEN
    #                                 INSERT INTO log (planned_maintenance, type, description) 
    #                                 VALUES ('2024-04-15','update','new2');
    #                             END IF;
    #                         RETURN NEW;
    #                     ELSIF TG_OP = 'INSERT' THEN
    #                             INSERT INTO log (planned_maintenance, type, description) 
    #                             VALUES ('2024-04-15','insert','new');
    #                         RETURN NEW;                        
    #                     ELSIF TG_OP = 'DELETE' THEN
    #                             INSERT INTO log (planned_maintenance, type, description) 
    #                             VALUES ('2024-04-15','delete','new');
    #                         RETURN OLD;
    #                     END IF;
    #                 END;
    #                $$ LANGUAGE plpgsql;
    #                """)

    cursor.execute("""CREATE TRIGGER t_change_table 
                   AFTER UPDATE OR INSERT OR DELETE ON cars --, car_condition, person
                   FOR EACH ROW
                   EXECUTE FUNCTION fn_change_in_table();
                """)
    
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

    # cursor.execute("""
    #                CREATE OR REPLACE FUNCTION select_new_cars(car_name varchar)
    #                RETURNS numeric AS 
    #                $$
    #                     SELECT COUNT (*) FROM  cars
    #                     WHERE brand like car_name and year >2020
    #                $$

    #                LANGUAGE SQL
    #                ;""")
    # cursor.execute("""DROP FUNCTION IF EXISTS newest_cars()  CASCADE;""")
    # cursor.execute("""
    #                 CREATE OR REPLACE FUNCTION newest_cars()
    #                RETURNS SETOF cars as
    #                $$
    #                 SELECT * FROM cars
    #                ORDER BY year DESC
    #                LIMIT 5;               
    #                $$
    #                LANGUAGE SQL   
    #             ;""")

    # cursor.execute(""" DROP FUNCTION IF EXISTS select_cars(varchar) CASCADE
    #             ;""")
    # cursor.execute(""" CREATE OR REPLACE FUNCTION select_cars(cars_name VARCHAR)
    #                RETURNS setof varchar AS
    #                $$
    #                DECLARE
    #                     car_brand VARCHAR;
    #                 BEGIN
    #                     FOR car_brand IN
    #                         SELECT brand
    #                         FROM cars
    #                         WHERE 
    #                         brand like cars_name
    #                     LOOP
    #                         RETURN NEXT car_brand;
    #                     END LOOP;
    #                     RETURN;
    #                 END;
    #                $$
    #                LANGUAGE PLPGSQL;
    #                """)
    
#     cursor.execute("""DROP FUNCTION IF EXISTS fn_get_sum(int, int) CASCADE;""")
#     cursor.execute(""" 
#                 CREATE OR REPLACE FUNCTION fn_get_sum(val1 int, val2 int)
#                     RETURNS int 
#                    AS
#                    $$
#                    DECLARE
#                         answear int;
#                    BEGIN
#                         answear := val1 +val2;
#                         RETURN answear;
#                     END;
#                    $$
#                 LANGUAGE PLPGSQL;
#                 """)

#     cursor.execute("""DROP FUNCTION IF EXISTS fn_get_random_val(int, int);
#                    """)
#     cursor.execute(""" 
#                 CREATE OR REPLACE FUNCTION fn_get_random_val(min_val int, max_val int)
#                     RETURNS float AS
#                     $$
#                     DECLARE
#                         rand float;
#                         another_val int;
#                     BEGIN
#                         SELECT random()INTO rand;
#                         RETURN rand;
#                     END;
#                     $$
#                   LANGUAGE PLPGSQL;
#                   """)

    # cursor.execute("""DROP FUNCTION IF EXISTS fn_get_sum_2(int, int) CASCADE; """)
    # cursor.execute("""
    #                CREATE OR REPLACE FUNCTION fn_get_sum_2(IN v1 int, IN v2 int, OUT answear int)  
    #                 AS $$
    #                 BEGIN
    #                     answear := v1 + v2;
    #                 END;
    #                 $$
    #                 LANGUAGE PLPGSQL""")
    # cursor.execute("""SELECT fn_get_sum_2(1,100);""")

    # cursor.execute(""" DROP FUNCTION IF EXISTS read_log() CASCADE;""")
    # cursor.execute(""" CREATE OR REPLACE FUNCTION read_log()
    #                     RETURNS TABLE(
    #                         day_log numeric,
    #                         month_log numeric
    #                     )
    #                     AS $$
    #                     BEGIN
    #                         RETURN QUERY
    #                         SELECT EXTRACT(DAY FROM planned_maintenance) AS "DAY", 
    #                                EXTRACT(MONTH FROM planned_maintenance) AS "MONTH"
    #                         FROM log
    #                         WHERE planned_maintenance = CURRENT_DATE
    #                         ORDER BY id DESC;
    #                     END;
    #                     $$
    #                     LANGUAGE PLPGSQL;
    #                """)
    
    # cursor.execute(""" DROP FUNCTION IF EXISTS check_log(int) CASCADE; """)
    # cursor.execute("""
    #                CREATE OR REPLACE FUNCTION check_log(the_month int)
    #                RETURNS varchar AS
    #                $$
    #                DECLARE
    #                 many_logs int;
    #                BEGIN
    #                 SELECT COUNT(id) INTO many_logs
    #                 FROM log
    #                 WHERE EXTRACT (MONTH FROM planned_maintenance ) = the_month;
    #                 IF many_logs < 3 THEN
    #                     RETURN CONCAT( many_logs, ' - lazy time');
    #                 ELSEIF many_logs >= 3 THEN
    #                     RETURN CONCAT(many_logs, '- work well');
    #                 ELSE
    #                     RETURN 'wrong value';
    #                 END IF;
    #                 END;
    #                 $$
    #                 LANGUAGE PLPGSQL;
    #                 ;""")

    cursor.execute(""" DROP FUNCTION IF EXISTS case_check_log( int) CASCADE; """)
    cursor.execute(""" CREATE OR REPLACE FUNCTION case_check_log( IN the_month int)
                   RETURNS varchar AS
                   $$
                   DECLARE
                   many_logs numeric;
                    BEGIN
                        SELECT count(*) INTO many_logs
                        FROM log
                        WHERE EXTRACT(MONTH FROM planned_maintenance)= the_month;
                        CASE
                            WHEN many_logs < 3 THEN
                                RETURN CONCAT( many_logs, ' - lazy time');
                            WHEN many_logs >= 3 THEN
                                RETURN CONCAT(many_logs, '- work well');
                            ELSE
                                RETURN 'wrong value';
                        END CASE;

                    END;
                    $$
                   LANGUAGE PLPGSQL;""")

except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)