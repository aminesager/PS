t=int(input())
while(t):
    t = t -1
    line = input("")
    n, m = map(int, line.split())

    a = input()
    b = input()
    
    b0 = b.count("0")
    b1 = b.count("1")

    s = ""
    c = 0
    for i in range(len(a)):
        s += a[i]
        if s.count("0") <= b0  and s.count("1") <= b1:
            c += 1
        else:
            break
        
    print(c)
