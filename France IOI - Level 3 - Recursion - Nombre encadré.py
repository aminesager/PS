def f(n, x):
    if x == 0:
        print(n,end='')
    if x>0:
        print("[",end='')
        f(n, x-1)
        print("]",end='')

    
    
f(42,2)