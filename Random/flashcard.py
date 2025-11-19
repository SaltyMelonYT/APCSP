import random

questions = {
    "Formula": {
        "correct": "type"
    }
}

def flashcards(dict):
    goneover=[]
    correct = []
    counter=1
    while len(dict)!=len(goneover):
        question=random.choice(list(questions.keys()))
        data=questions[question]
        if question in goneover:
            pass
        else:
            print(question)
            dict(*data["choices"], data["correct"], correct)
            goneover.append(question)
            counter +=1
    print("You got", len(goneover),"correct.")

flashcards(questions)