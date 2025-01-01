def pal(n):
    original = n
    inverse = 0
    
    while n > 0:
        inverse = inverse * 10 + n % 10
        n = n // 10
    
    return original == inverse

print(pal(88888))