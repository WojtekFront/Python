from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
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

