t= int(input())
 
 
while(t):
    line = input("")
    t = t -1
    a, b, c= map(int, line.split())
    
    mini = min(a, b, c)
    maxi = max(a, b, c)
    mid = a+b+c - maxi - mini
    
    
    for i in range(5):
        mini = mini +1
        if mini > mid:
            aux = mini
            mini = mid
            mid = aux
        if mid > maxi:
            aux = maxi
            maxi = mid
            mid = aux
            
            
    print(mini*mid*maxi)