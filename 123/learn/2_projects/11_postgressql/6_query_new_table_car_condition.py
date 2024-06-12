from conn import connect_to_db, close_connction
from datetime import date, timedelta
import random

random_car_id = random.randint(1,25)
random_insurance = random.randint(-50, 365)
insurance_date   =  date.today() + timedelta(days=random_insurance)

random_maintenance = random.randint(-50, 365)
maintenance_date = date.today()+timedelta(days=random_maintenance)
print()

print(insurance_date)
print(maintenance_date)

""" open connection"""
connection, cursor = connect_to_db()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS car_condition(
                   id SERIAL PRIMARY KEY,
                   car_id INTEGER NOT NULL,
                   planned_maintenance DATE NOT NULL,
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