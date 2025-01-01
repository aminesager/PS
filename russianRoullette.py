from random import randint

T=[]
death = (randint(1, 6))

while len(T)!=6 :
    a = (randint(1, 6))
    print("give name")
    name = input("Enter name : ")
    if a not in T :
        T.append(a)
        if a == death :
            print(dead)
        
        