for i in range(int(input())):
    a, b, c = map(int, input().split())
    
    
    if (c+b+a) % 2 == 0:
        s = 0
        s += a
        while a!= 0:
            if b<c:
                c -= 1
            else:
                b -= 1
            a -= 1
        print(s+min(b,c))
    else:
        print(-1)
        
"""
this also works better as well
for i in range(int(input())):
    a, b, c = map(int, input().split())
    
    
    if (c+b+a) % 2 == 0:
        print(min((a+b+c)//2,a+b))
        
    else:
        print(-1)
"""