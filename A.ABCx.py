
        
t = int(input())
while(t):
    t=t-1
    n = int(input())
    s  = input()
    
    if len(s) == 1:
        print("YES")
    elif len(s) == 2:
        if s[0] == s[1]:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
        
    
    