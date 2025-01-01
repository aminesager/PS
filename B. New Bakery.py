for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s=0
    if b<=a:
        s = n*a
    elif b-n >= a:
            s = ((n) * (b-n+1 +b)) // 2
    else:
        s = abs(n-(b-a))*a
        s +=  ((b-a) * (b-n+1+s//a + b)) // 2
            
    print(s)