class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
    
    def add_name(self, name):  
        self.name = str(name)

    def add_grade(self, grade):
        self.grades.append(grade)

    def on_honor_roll(self):
        if not self.grades:
            return False
        ave_grade = sum(self.grades) / len(self.grades)
        return ave_grade >= 3
        
