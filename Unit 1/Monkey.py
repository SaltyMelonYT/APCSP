# Coding Challenge Unit 1.1
monkey_name = input("Monkley's name is: ")
current_bananas = 150
consumed_bananas = 50
password = "I<3bananas"
remaining_bananas = current_bananas - consumed_bananas
attempt = input("Please enter super secret password: ")

if attempt == password:
    print(f"{monkey_name} consumed {consumed_bananas} bananas and has {remaining_bananas} bananas left.")
else:
    print("Denied.")