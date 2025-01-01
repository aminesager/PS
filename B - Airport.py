a, b = map(int, input().split())
P = list(map(int, input().split()))
P1 = P.copy()
 
sMin = 0
P.sort()
for i in range(a):
    if P[0] == 0:
        P.remove(0)
        
    sMin += P[0]
    P[0] -= 1
    
    
 
 
 
sMax = 0
for i in range(a):
    sMax += max(P1)
    
    P1.sort()
    P1[b-1] -= 1
    
print(sMax, sMin)
 