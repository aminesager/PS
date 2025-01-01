def water(n):
    a=0
    b=0
    if n%2 == 0:
        a = n//2 -1
        b = n//2 +1
        if a%2 != 0:
            print(a, b)
        while(a != 0):
            b=b+1
            a=a-1
            if a%2 != 0:
                print(a, b)
            
    else:
        return 'Noo'
    
n = int(input("Enter a random number:"))
print(water(n))
