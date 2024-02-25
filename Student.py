class Student:
    def __init__(self, name, grades: list):
        self.name = name
        self.grades = [grades]
    
    def add_name(self, name):  
        self.name = name

    def add_grade(self, grades):
        self.grades.append(grades)


