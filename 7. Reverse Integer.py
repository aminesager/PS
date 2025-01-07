def reverse(x):
    if x>=0: 
        nb = int(str(x)[::-1])
    else:
        nb = -int(str(x)[1:][::-1])
    
    interval = (2**32)
    print(interval>nb)
    if -1*interval < nb < interval:
        return nb
    else:
        return 0
    
print(reverse(1534236469))