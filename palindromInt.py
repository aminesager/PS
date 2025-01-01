def pal(n):

    i=0
    T=[]
    while n != 0 :
        last_digit = n % 10
        n = n // 10
        T.append(last_digit)
        i += 1
    
    for j in range(i // 2):
        if T[j] != T[i - j - 1]:
            return False
    return True
    
print(pal(1441))