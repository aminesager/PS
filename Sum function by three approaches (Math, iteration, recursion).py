def mathematical(n):
    return n*(n+1)//2

def iterative(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
        
def recursive(n):
    if n == 1:
        return 1
    else:
        return n+ recursive(n-1)
    
    
n = 100
print(mathematical(n))
print(iterative(n))
print(recursive(n))
