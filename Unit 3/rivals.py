def rivals(name1, name2):
    len1=len(name1)
    len2=len(name2)
    name1lives=3
    name2lives=3

    if len1>len2: # The first name is longer
        print(name1,"is the winner")
        name2lives=name2lives-1
    elif len1 == len2: # Names are equal lengths
        print("It is a tie")
    else: # The second name is longer
        print(name2,"is the winner")
        name1lives=name1lives-1

rivals(input("Name 1: "), input("Name 2: "))

