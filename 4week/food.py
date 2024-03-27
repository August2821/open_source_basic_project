f1=["tteokbokki", "jajangmyeon", "ramen", "pizza", "beer", "chicken", "pork belly"]
f2=["fish cake", "pickled radish", "kimchi", "pickles", "chicken", "beer", "lettuce"]


while 1:
    name=input("What's your favorite food among tteokbokki, jajangmyeon, ramen, pizza, beer, chicken, and pork belly? ")
    flag=0
    for i in range(7):
        if name==f1[i]:
            print("The food that goes well with <",f1[i],"> is <",f2[i],">.")
            flag+=1
            break
    if flag==0:
        print("There is no such food. Check it out.")
    if name=="end":
        break