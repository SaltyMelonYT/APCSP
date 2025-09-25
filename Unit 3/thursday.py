import time

def add(a,b):
    print("Adding numbers...")
    time.sleep(0.9)
    print("One second...")
    time.sleep(0.8)
    print("Almost there...")
    time.sleep(0.7)
    print("Done! Your answer is", a+b)

def factorial(a):
    sum=1
    for i in range(a):
        if a > 1:
            sum=sum*a
            a=a-1
            print(sum)

def pi(length):
    approx_pi=20/6.336
    pi_str=str(approx_pi)[:length+2]
    print(pi_str)
    print("The length of the original equation:",len(str(approx_pi)))
    print("The length of the output: ", len(pi_str))

pi(2)