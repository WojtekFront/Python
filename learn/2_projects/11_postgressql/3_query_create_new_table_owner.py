from conn import connect_to_db, close_connction
import random

new_firstname = random.choice([ "Agnieszka", "Amelia", "Andrzej", "Anna", "Ava", "Barbara", "Charles", "Charlotte",
    "Daniel", "David", "Dorota", "Edward", "Eleanor", "Eliza", "Emma", "Emily",
    "Ewa", "Evelyn", "Ethan", "Fiona", "Franciszek", "Gabriel", "Grace", "Grzegorz",
    "Hanna", "Henry", "Isabella", "Izabela", "Jacob", "James", 
    "Jan", "Joanna", "John", "Joseph", "Julia", "Kacper", "Kamil", "Katarzyna",
    "Krzysztof", "Laura", "Liam", "Liliana", "Lucas", "Magdalena", "Maja", 
    "Marek", "Maria", "Marcin", "Mary", "Mateusz", "Matthew", "Michael", 
    "Mia", "Michał", "Monika", "Natalia", "Nathan", "Nikola", "Olivia", 
    "Oliwia", "Oskar", "Paweł", "Piotr", "Rachel", "Robert", "Ryszard",
    "Sara", "Sophia", "Stanisław", "Stefan", "Susan", "Thomas", "Tomasz",
    "Victoria", "William", "Wojciech", "Zofia", "Zuzanna"])
new_lastname = random.choice([    "Allen", "Anderson", "Baker", "Baran", "Brown", "Chmielewski", "Clark", "Davis", 
    "Dąbrowski", "Evans", "Garcia", "Grabowski", "Green", "Hall", "Hill", "Jankowski", 
    "Johnson", "Jones", "Kaczmarek", "Kamiński", "Kowalczyk", "Kowalski", "Kozłowski", 
    "Krawczyk", "Kwiatkowski", "Lee", "Lewandowski", "Lewis", "Mazur", "Michalski", 
    "Miller", "Murphy", "Nowak", "Pawlak", "Smith", "Szewczyk", "Szymański", "Taylor", 
    "Thompson", "Walker", "White", "Wiśniewski", "Wilk", "Wilson", "Woźniak", "Wójcik", 
    "Wright", "Young", "Zając", "Zielińska", "Zieliński"])
new_age = random.randrange(18,75)


# print(new_firstname, new_secondname, new_age)
""" open connection"""
connection, cursor = connect_to_db()


# firstname 
# secondname
# age
try:
    # cursor.execute("""CREATE TABLE IF NOT EXISTS person(
    #     id SERIAL PRIMARY KEY,
    #     firstname varchar(50),
    #     lastname varchar(50),
    #     age int              
    # )  
    #     ;""")

    # for i in range(20):
    #     i+=1
    #     new_firstname = random.choice([ "Agnieszka", "Amelia", "Andrzej", "Anna", "Ava", "Barbara", "Charles", "Charlotte",
    #     "Daniel", "David", "Dorota", "Edward", "Eleanor", "Eliza", "Emma", "Emily",
    #     "Ewa", "Evelyn", "Ethan", "Fiona", "Franciszek", "Gabriel", "Grace", "Grzegorz",
    #     "Hanna", "Henry", "Isabella", "Izabela", "Jacob", "James", 
    #     "Jan", "Joanna", "John", "Joseph", "Julia", "Kacper", "Kamil", "Katarzyna",
    #     "Krzysztof", "Laura", "Liam", "Liliana", "Lucas", "Magdalena", "Maja", 
    #     "Marek", "Maria", "Marcin", "Mary", "Mateusz", "Matthew", "Michael", 
    #     "Mia", "Michał", "Monika", "Natalia", "Nathan", "Nikola", "Olivia", 
    #     "Oliwia", "Oskar", "Paweł", "Piotr", "Rachel", "Robert", "Ryszard",
    #     "Sara", "Sophia", "Stanisław", "Stefan", "Susan", "Thomas", "Tomasz",
    #     "Victoria", "William", "Wojciech", "Zofia", "Zuzanna"])
    #     new_lastname = random.choice([    "Allen", "Anderson", "Baker", "Baran", "Brown", "Chmielewski", "Clark", "Davis", 
    #     "Dąbrowski", "Evans", "Garcia", "Grabowski", "Green", "Hall", "Hill", "Jankowski", 
    #     "Johnson", "Jones", "Kaczmarek", "Kamiński", "Kowalczyk", "Kowalski", "Kozłowski", 
    #     "Krawczyk", "Kwiatkowski", "Lee", "Lewandowski", "Lewis", "Mazur", "Michalski", 
    #     "Miller", "Murphy", "Nowak", "Pawlak", "Smith", "Szewczyk", "Szymański", "Taylor", 
    #     "Thompson", "Walker", "White", "Wiśniewski", "Wilk", "Wilson", "Woźniak", "Wójcik", 
    #     "Wright", "Young", "Zając", "Zielińska", "Zieliński"])
    #     new_age = random.randrange(18,75)

    #     cursor.execute("""INSERT INTO person (firstname, lastname, age) VALUES(%s, %s, %s);""",(new_firstname, new_lastname, new_age))
    cursor.execute(""" ALTER TABLE person ADD COLUMN car_id INTEGER;
                   
                   """)
    cursor.execute("""
                   ALTER TABLE person 
                   ADD CONSTRAINT fk_car
                   """)

    cursor.execute("""SELECT * FROM person 
        """)
    result = cursor.fetchall()
    for row in result:
        print(row)
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)