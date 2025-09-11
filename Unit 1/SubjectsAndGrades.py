subjects = []
grades = []
numSub = int(input("How many subjects do you have? Please enter a number: "))
for int in range(numSub):
    Class = input("What subject? ")
    Score = float(input("Grade for that class? "))
    subjects[Class]=Score
    
print(f"Your subjects are\n{subjects}")
print(f"Your grades are\n{grades}")
