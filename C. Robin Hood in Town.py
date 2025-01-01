for i in range(int(input())):
    n = int(input())
    T = list(map(int, input().split()))
    
    
    if n<= 2:
        print(-1)
    else:
        T.sort()
        robin = n//2
        mid = T[robin]
        target = 2*T[robin]
        s = sum(T)
        avg = s / n
        
        if  mid < (avg/2) :
            print(0)
        else:
            print(1 + mid*2*n - s)
            
        
        