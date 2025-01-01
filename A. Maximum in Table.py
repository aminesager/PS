n = int(input())

m = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    m[0][i] = 1

def sum(m,i,j):
    s=0
    for x in range(j):
        s=s+m[i-1][x]
    return s
    


for i in range(1,n):
    for j in range(n):
        if j == 0:
            m[i][j] = 1
        else:
            m[i][j] = sum(m,i,j+1)
    
print(m[n-1][n-1])
