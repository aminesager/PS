t = int(input())
while(t):
    t=t -1
    n = int(input())
    k = int(input())
    grid=""
    for i in range(n):
        g = input()
        grid += g
        
    newN = n//k
    
    g = ""
    for i in range(0,n*n,k):
        g += grid[i]
    
    print(g)
    
    