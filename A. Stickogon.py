for _ in range(int(input())):
    n = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T1 = set(T)
    s=0
    for stick in T1:
        s += T.count(stick) // 3
    print(s)
    
    