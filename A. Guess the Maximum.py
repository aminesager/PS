for _ in range(int(input())):
    n = int(input())
    T = list(map(int, input().split()))
    k = max(T)
    for i in range(n-1):
        val = max(T[i], T[i+1])
        if val < k :
            k = val
        
    print(k-1)