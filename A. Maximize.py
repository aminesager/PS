def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
while(t):
    t=t -1
    x = int(input())
    print(x-1)

