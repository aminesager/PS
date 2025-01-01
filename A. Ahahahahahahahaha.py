for _ in range(int(input())):
    n = int(input())
    line = input()
    c1 = line.count("1")
    c0 = line.count("0")
    
    if c0 >= c1:
        res = "0" * c0
        l = c0
    else:
        res = "1" * (c1 - c1%2)
        l = c1 - c1%2
            
    print(l)       
    print(" ".join(res))