def area(l,w):
    area=l*w
    print("area:",area)
    return area

def add(a,b,c):
    print('total:',a+b+c)
    return a+b+c

def base10Converstion(bits):
    binary=[]
    subFac=128
    if bits==0:
        binary.append("0")
    else:
        for i in range(8):
            if bits-subFac>=0:
                binary.append("1")
                bits=bits-subFac
            else:
                if len(binary)!=0:
                    binary.append("0")
            subFac=subFac//2
    print("binary:","".join(binary))

def base2Converstion(bits):
    power=1
    total=0
    for i in range(len(str(bits))):
        R=bits%10
        total=total+R*power
        power=power*2
        bits=bits//10
    print(total)

binary=base10Converstion(add(area(1,2),area(3,4),area(5,6)))
