import json

class My_app:
    def __init__(self, filepath):
        self.filepath = filepath
        self.quiz_questions = self.load_questions()
        
    def load_questions(self):
        # Assuming the file content is a JSON string similar to the quiz_questions array you provided.
        with open(self.filepath, "r") as file:
            questions = json.load(file)
        return questions
    
    def display_question(self, question):
        print(question["Question"])
        for option in question["Options"]:
            print(option)
        user_answer = input("Your answer: ")
        return user_answer.strip().lower()
    
    def run_quiz(self):
        for question in self.quiz_questions:
            user_answer = self.display_question(question)
            correct_answer = question["Correct Answer"][0].lower()
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print("Incorrect! The correct answer is:", question["Correct Answer"][1])
            print("English Rule:", question["English Rule"])
            print()

# Create an instance of My_app and run the quiz
# INCORRECT ADRESS
app = My_app(r"..\Python\sup\csv\english1.csv")

app.run_quiz()
