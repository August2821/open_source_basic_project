# 종합계산기
check=int(input("1. Calculate the entered formula  2. the sum between two numbers : "))

def sum1(a,b):
    sum: int=0
    for i in range(a,b+1,1):
        sum=sum+i
    print("The sum of ",a,"to",b,"is",sum)

if check==1:
    formula=input("Enter a formula: ")
    print("It's",eval(formula))

if check==2:
    a=int(input("Please enter the first number: "))
    b=int(input("Please enter the second number: "))
    sum1(a,b)
    