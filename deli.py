def suite(n):
    if n == 0 or n == 1:
        return 1
    else:
        return suite(n-1) + suite(n-2)
    
    
print(suite(6))