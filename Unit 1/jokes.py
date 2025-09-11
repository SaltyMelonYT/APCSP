import random
jokes=["joke 1", "joke 2", "joke 3", "joke 4"]
amount=len(jokes)
for i in range(amount):
    print("jokes available: ", amount)
    num=random.randrange(amount)
    print(jokes[num])
    input()