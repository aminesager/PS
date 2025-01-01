for _ in range(int(input())):
    l, r = map(int, input().split())
    L, R = map(int, input().split())


#calculate nb of rooms where both can exist
    
    maxLeft = max(l, L)
    maxRight = min(r, R)
    
    c = max(0, maxRight - maxLeft +1)
    
    if r==R and l ==L:
        print(c-1)
    elif c ==0:
        print(1)
    elif R==r or l==L:
        print(c)
    else:
        print(c+1)