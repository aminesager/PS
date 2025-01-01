t= int(input())
while(t):
    t=t-1

    n = int(input())
    line = input("")
    T = list(map(int, line.split()))
        

    a=[1000]
    for i in range(1,n):
        a.append(a[i-1]+T[i-1])
    
    result = ' '.join(map(str, a))
    print(result)

