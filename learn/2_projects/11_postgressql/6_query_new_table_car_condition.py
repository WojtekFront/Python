from conn import connect_to_db, close_connction


""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS car_condition(
                   id SERIAL PRIMARY KEY,
                   car_id INTEGER NOT NULL,
                   planned_maintance DATE NOT NULL,
                   insurance_validity DATE NOT NULL,
                   insurance_value MONEY DEFAULT 0,
                   had_accident BOOLEAN DEFAULT FALSE NOT NULL,
                   country_of_origin VARCHAR(30)
                    )
                   ;""")
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

