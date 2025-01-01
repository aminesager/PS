def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    start = s.find('0')
    end = s[::-1].find('0')
    z = s[start:n-end]
    
    if is_prime(n):
        print('No')
    elif start == -1 :
        print('Yes')
    elif(z[::-1] == z):
        print('Yes')
    else:
        print('No')