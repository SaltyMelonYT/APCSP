numList=[1,2,2,3,3,3,3,3]
numDict={}

for i in numList:
    if i not in numDict:
        numDict[i]=1
    else:
        numDict[i]+=1

print(numDict)