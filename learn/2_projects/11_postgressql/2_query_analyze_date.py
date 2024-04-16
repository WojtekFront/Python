from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""
                   SELECT * FROM cars
                   ;""")
    # cursor.execute("""SELECT AVG(year)::NUMERIC(10,0) FROM cars
    #                ;""")
    # cursor.execute("""
    #                SELECT * FROM cars WHERE brand LIKE 'a%'
    #                ;""")
    # cursor.execute("""
    #                SELECT DISTINCT brand FROM cars WHERE brand  in ('AUDI', 'FORD')
    #                ;""")
    # cursor.execute("""
    #                SELECT c.id, c.* FROM cars as c WHERE id not IN (SELECT id FROM cars WHERE brand ILIKE 'a%' limit 5)
    #                ;""")
    # cursor.execute("""
    #                SELECT c.id, c.brand || ' ' || c.model, c.* FROM cars c 
    #                WHERE id IN (
    #                   SELECT id FROM cars 
    #                      WHERE brand ILIKE 'a%' AND id BETWEEN 10 and 15 LIMIT 5)
    #                ORDER BY c.id
    #                ;""")
    # cursor.execute("""
    #                SELECT c.* FROM cars c
    #                WHERE NOT EXISTS (
    #                SELECT p.id FROM person p
    #                WHERE p.car_id = c.id
    #                AND p.car_id = 1
    #                )
    #                ;""")
    # cursor.execute("""
    #                SELECT round(AVG(year)) FROM cars
    #                ;""")
    # cursor.execute("""SELECT COUNT(brand) FROM cars WHERE brand = 'FORD'
    # ;""")
    # cursor.execute("""
    #                Select* FROM cars;
    #                """)
    # cursor.execute("""
    #                SELECT year, brand, model FROM cars WHERE year > 2010 ORDER BY year LIMIT 3;
    #                """)
    # cursor.execute("""
    #                  SELECT DISTINCT color FROM cars ORDER BY color;
    #               """)
    # cursor.execute("""
    #                SELECT id FROM cars OFFSET 5
    #                """)


    result = cursor.fetchall()
    for row in result:
        print(row)

except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

