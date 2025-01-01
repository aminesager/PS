def max(T, n):
    if n == 0 :
        return (T[0])
    
    if T[n] > T[0]:
        T[0] = T[n]
    
    
    if n > 0:
        return max(T, n-1)

T = [5,7,6,0,1,4,33,4,2,10,8]


print("Maximum element in the array is:", max(T, len(T)-1))