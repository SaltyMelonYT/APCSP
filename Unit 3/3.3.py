def convert(bits):
    power=1
    total=0
    strBits=str(bits)
    times=len(strBits)
    for i in range(times):
        R=bits%10
        total=total+R*power
        power=power*2
        bits=bits//10
    print(total)

convert(1000011)