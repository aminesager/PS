for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a % 2 == 0:
        if b == 0 or b%2 == 0:
            print('Yes')
        elif b%2 == 1 and a>= 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
        