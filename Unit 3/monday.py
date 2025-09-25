num1=int(input("Your first number? "))
num2=int(input("Your second number? "))
nums=[]
nums.append(num1)
nums.append(num2)
nums.sort()
larger=nums[-1]
smaller=nums[-2]
print(larger)
print(smaller)
if smaller==0:
    print("These numbers are not divisble")
else:
    print(larger/smaller)