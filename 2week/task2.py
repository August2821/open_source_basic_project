system=int(input("Determining the input essence(16/10/8/2): "))
number=input("value: ")


if system ==10:
    num=int(number,10)
    print("16 essence ==>",hex(num))
    print("10 essence ==>",num)
    print("8 essence ==>",oct(num))
    print("2 essence ==>",bin(num))
    
elif system==2:
    num=int(number,2)
    print("16 essence ==>",hex(num))
    print("10 essence ==>",num)
    print("8 essence ==>",oct(num))
    print("2 essence ==>",bin(num))
    
elif system==8:
    num=int(number,8)
    print("16 essence ==>",hex(num))
    print("10 essence ==>",num)
    print("8 essence ==>",oct(num))
    print("2 essence ==>",bin(num))
    
elif system==16:
    num=int(number,16)
    print("16 essence ==>",hex(num))
    print("10 essence ==>",num)
    print("8 essence ==>",oct(num))
    print("2 essence ==>",bin(num))
