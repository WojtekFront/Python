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
new_secondname = random.choice([    "Allen", "Anderson", "Baker", "Baran", "Brown", "Chmielewski", "Clark", "Davis", 
    "Dąbrowski", "Evans", "Garcia", "Grabowski", "Green", "Hall", "Hill", "Jankowski", 
    "Johnson", "Jones", "Kaczmarek", "Kamiński", "Kowalczyk", "Kowalski", "Kozłowski", 
    "Krawczyk", "Kwiatkowski", "Lee", "Lewandowski", "Lewis", "Mazur", "Michalski", 
    "Miller", "Murphy", "Nowak", "Pawlak", "Smith", "Szewczyk", "Szymański", "Taylor", 
    "Thompson", "Walker", "White", "Wiśniewski", "Wilk", "Wilson", "Woźniak", "Wójcik", 
    "Wright", "Young", "Zając", "Zielińska", "Zieliński"])
new_age = random.randrange(18,75)


print(new_firstname, new_secondname, new_age)
""" open connection"""
connection, cursor = connect_to_db()


# firstname 
# secondname
# age

try:
    cursor.execute("""SELECT * FROM cars LIMIT 1
        """)
except Exception as error:
    print(f"{error}")

finally:
    """Commit and close"""
    connection.commit()
    close_connction(connection, cursor)

