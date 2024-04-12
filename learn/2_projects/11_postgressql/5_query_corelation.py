from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    
    cursor.execute(""" 
        SELECT p.car_id, COUNT(p.car_id), c.brand 
            FROM person as p
            JOIN cars as c ON p.car_id = c.id
            
            GROUP BY p.car_id, c.brand
                   
            HAVING  COUNT(P.car_id) > 1
            ORDER BY p.car_id;
    """)
    # cursor.execute(""" 
    #     SELECT p.car_id, c.brand 
    #         FROM person as p
    #         JOIN cars as c ON p.car_id = c.id
            
    # """)

    result = cursor.fetchall()
    for row in result:
        print(row)
except Exception as error:
    print(f"Błąd::  {error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

