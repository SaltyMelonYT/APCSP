grades = []

for i in range(10):
    score = int(input(f"What was your grade? {i+1}/10 "))
    grades.append(score)

grades.sort()
print(f"Your highest was {grades[9]}")
print(f" Your avergae is {sum(grades)/10}")
print(f"Your lowest is {grades[0]}")