def favMovies(prompt, list, debug=3):
    count=0
    print("Type 'stop' to stop the program")
    fullPrompt=prompt+" "
    while True:
        if count==debug:
            print("REMINDER!\nType 'stop' to stop the program")
            count=0

        a=input(fullPrompt)
        
        if a.lower() == "stop":
            print("You have",len(list),"favorite movies! Quitting now")
            break
        elif a.lower()=="list":
            print(list)
        elif a in list:
            print("This movie is already in the list! Add it anyways? ")
            confirm=input("y/N ")
            if confirm.lower()=='y':
                list.append(a)
        else:
            list.append(a)
            count=count+1
movies=[]
favMovies("What are your favorite movies? List one by one.", movies, 5)