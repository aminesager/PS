for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    pair=0
    imp=0
    for i in range(len(t)):
        if t[i] % 2 == 1:
            imp += 1
        else:
            pair +=1
    if pair == imp :
        print('Yes')
    else:
        print('No')