import random
questionBank={
    1:{"question":"What is 2+2","answer":"4"},
    2:{"question":"What is 3+3","answer":"6"},
    3:{"question":"What is 4+4","answer":"8"}
}

def proto1():
    score=0
    for i in range(len(questionBank)):
        print(questionBank[i+1]["question"])
        answer=input()
        if answer==questionBank[i+1]["answer"]:
            score+=1
        else:
            pass
    print(score)

def proto2():
    score=0
    nums=[1,2,3]
    while nums:
        question=random.randint(1,3)
        if question in nums:
            nums.remove(question)
            print(questionBank[question]["question"])
            answer=input()
            if answer==questionBank[question]["answer"]:
                score+=1

    print(score)

proto2()