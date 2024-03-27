name=input("Enter a string:")
length=len(name)

print("Output content backwards: ",end="")
for i in range(length-1,-1,-1):
    print(name[i],end="")
print()
