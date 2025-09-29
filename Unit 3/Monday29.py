def listAdd(text, list, debug=3, length=False):
    count=debug
    while True:
        if count==debug:
            print("type stop to stop program, list to show the list, or remove to remove a name.")
            count=0
        ask=input(text+" ")
        if ask.lower()=="stop":
            break
        elif ask.lower()=="list":
            print(list)
        elif ask.lower()=="remove":
            while True:
                remove=input("Who to remove? ")
                if remove not in list:
                    print("Name not found, check spelling and capitalization")
                else:
                    list.remove(remove)
                    break
        elif ask.lower()=='':
            print("Name is blank! Will not append")
        elif ask in list:
            confirm=input("This name is already in the list, add anyway? y/N ")
            if confirm.lower()=="y":
                list.append(ask)
            else:
                pass
        else:
            list.append(ask)
        count=count+1

    if length==True:
        print("You have",len(list),"friends")
Friends=[]
listAdd("Name of person?", Friends, 5)