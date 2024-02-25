from Question import Question


questions_prompts = [
    "What color are apples?\na) red\nb) blue\nc) black\nd) purple\n\n",
    "What color are bananas?\na) red\nb) blue\nc) green\nd) yellow\n",
    "What color are strawberries?\na) red\nb) blue\nc) green"
]

questions = [
   Question(questions_prompts[0], "a"),
   Question(questions_prompts[1], "d"),
   Question(questions_prompts[2], "1")
   ]

def ask_question(questions): # pylint: disable= operator 
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1        
    print(f"You got {score} out of {len(questions)} questions correct.")

ask_question(questions)
   


