for _ in range(int(input())):
    l, r = map(int, input().split())
    '''
solution 1
    i= l
    p = 1
    while i<r:
        i += p
        p +=1 
    print(p if i==r else p-1)
    '''
    
    
    '''
solution 2
    d = r-l
    i=0
    while(i*(i+1)//2) <= d:
        i+=1
    print(i)
    ''''