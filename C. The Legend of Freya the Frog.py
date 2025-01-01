for _ in range(int(input())):
    x, y, k = map(int, input().split())
    s = max(x//k, y //k)
    if x%k != 0 or y%k != 0:
        s+= 1
    if x%k == 0 and y%k == 0 and y!= x:
        print(s*2 -1)
    else:
        print(s*2)