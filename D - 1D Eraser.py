t=int(input())
while(t):
    t=t-1
    line= input()
    n, k = map(int, line.split())
    chaine = input()
    op = 0
    countb = 0
    for i in range(len(chaine)):
        if countb == k:
            countb = 0
 
        if chaine[i] == "W":
            countb = 0
            
        if chaine[i] == "B":
            if countb == 0 :
                op += 1
            countb += 1
 
    print(op)
 