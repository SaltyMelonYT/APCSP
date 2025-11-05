def base2(bits):
    power=1
    total=0
    for i in range(len(str(bits))):
        R=bits%10
        total=total+R*power
        power=power*2
        bits=bits//10
    print(total)

def base10(bits):
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
    print("".join(binary))

base2(11000011010100000)

base10(67)
###############################################
def alternate(bits):
    binary=''
    while bits > 0:
        if bits % 2 == 1:
            binary="1"+binary
            bits=bits-1
        else:
            binary="0"+binary
        bits=bits/2
        print(binary)
    print(binary)

alternate(50)
