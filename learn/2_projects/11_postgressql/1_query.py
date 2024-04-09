from conn import connect_to_db, close_connction
import random


# cars_brand = random.choice(["AUDI", "BMW", "FORD"])
# if not cars_brand:
#     new_value = "Error beceause is empty"
# elif cars_brand == "AUDI":
#     cars_model = random.choice(["A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "R8"])
# elif cars_brand == "BMW":
#     cars_model =random.choice(["1 Series", "3 Series", "5 Series", "7 Series", "X1", "X3", "X5", "Z4", "i3", "i8"])
# elif cars_brand == "FORD":
#     cars_model = random.choice(["Fiesta", "Focus", "Mustang", "Explorer", "F-150", "Mondeo", "Ranger"])    
# else:
#     new_value = "not correct value "+cars_brand    

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

cars_brand2 = random.choice(list(cars_options.keys()))
cars_model1 = random.choice(cars_options[cars_brand])     

cars_data = 2000 + random.randrange(1, 24)

""" open connection"""
connection, cursor = connect_to_db()
 
try:

    cursor.execute("""
        INSERT INTO cars(brand, model, year, color) VALUES(%s, %s, %s, %s)""",(cars_brand, cars_model, cars_data, cars_color)           
        )
    # cursor.execute("""
    #     INSERT INTO cars(brand, model, year) VALUES(%s, %s, %s)""",(cars_brand, cars_model, cars_data)           
    #     )
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

