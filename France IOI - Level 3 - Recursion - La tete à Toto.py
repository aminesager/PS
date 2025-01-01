def toto(n):
    if n == 0 :
        print ('0',end='')
        return 0
    print('(',end='')
    toto(n-1)
    print('+',end='')
    toto(n-1)
    print(')',end='')
    
print(" 0 = ",end='')
toto(2)
