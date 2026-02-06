quiz={
    'question 1':'answer 1',
    'question 2':'answer 2',
    'question 3':'answer 3'
}

for key,value in quiz.items():
    ans=input(f'{key} ')
    if ans==value:
        print("Correct")