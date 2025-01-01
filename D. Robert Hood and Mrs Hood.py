for _ in range(int(input())):
    n, d, k = map(int, input().split())
    days = [""]*n
    c = 1
    for i in range(k):
        start, end = map(int, input().split())
        
        
        for k in range(start, end+1):
            days[k-1] = days[k-1] +  str(c)
        c+=1
 
    bro = 0
    mom = 1000000
    indB = 0
    indM = 0
    for i in range(0, n-d):
        ax = ''.join(days[i:i+d])
        ax = ''.join(sorted(set((ax))))
        if len(ax) > bro:
            bro = len(ax)
            indB = i
        if len(ax) <= mom:
            mom = len(ax)
            indM = i
    
    print(indB+1, indM+1)