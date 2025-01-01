t= int(input())
 
 
while(t):
    cond = False
    line = input("")
    t = t -1
    a, b, c, d = map(int, line.split())

    if a>b:
        max1=a
        min1=b
    else:
        max1=b
        min1=a
        
 
 
    if c in range(min1,max1) and d not in range(min1,max1):
        cond = True
            
    
    if d in range(min1,max1) and c not in range(min1,max1):
        cond = True
            
            
    if cond :
        print("yes")
    else:
        print("no")