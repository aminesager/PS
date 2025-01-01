n, k = map(int, input().split())
T = list(range(1, n+1, 1))  
print(*(T) if k == 0 else ((T[0:n-k-1] + (T[n-k-1:n])[::-1])))
