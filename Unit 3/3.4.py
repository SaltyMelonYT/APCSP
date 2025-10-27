def convert(match):
    bits='0'
    num=int(bits)
    total=0
    power=1

    while total!=match and total<match:
        R=num%10
        total=total+R*power
        power=power*2
        num=num//10
        if total!=match:
            if num%10==0:
                bits=bits+'1'
            elif num%10==1:
                bits=bits+'0'
        print(total)
        print(bits)
    print(total)



age=16
