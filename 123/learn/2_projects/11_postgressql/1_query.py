from conn import connect_to_db, close_connction
import random

cars_options = {
    "AUDI": ["A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "R8"],
    "BMW": ["1 Series", "3 Series", "5 Series", "7 Series", "X1", "X3", "X5", "Z4", "i3", "i8"],
    "FORD": ["Fiesta", "Focus", "Mustang", "Explorer", "F-150", "Mondeo", "Ranger"]
}
cars_brand = random.choice(list(cars_options.keys()))
cars_model = random.choice(cars_options[cars_brand])
cars_color = random.choice([
    "Beżowy", "Biały", "Bordowy", "Brąz", "Brązowy", "Brzoskwiniowy", "Burgund", 
    "Cyjan", "Czarny", "Fioletowy", "Fiołkowy", "Granatowy", "Indygo", "Lawendowy", 
    "Limonkowy", "Miętowy", "Morski", "Niebieski", "Oliwkowy", "Piaskowy",  
    "Pomarańczowy", "Różowy", "Srebrny", "Szary", "Turkusowy", "Zielony", 
    "Złoty", "Żółty"
])

cars_price = 1000 * random.randrange(20, 200)
cars_milage = 10000 * random.randrange(5, 400)
cars_data = 2000 + random.randrange(1, 24)

""" open connection"""
connection, cursor = connect_to_db()
 
try:
    cursor.execute("""
        INSERT INTO cars(brand, model, year, color, mileage, price_gross) VALUES(%s, %s, %s, %s , %s, %s)""",(cars_brand, cars_model, cars_data, cars_color, cars_milage, cars_data)           
        )

    cursor.execute("""
        SELECT * FROM cars
        """)

    results = cursor.fetchall()
    for row in results:
        print(row)
except Exception as error:
    print(f"{error}")
finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)