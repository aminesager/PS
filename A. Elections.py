n, m = map(int, input().split())

cityWin = [0]*n

for x in range(m):
    T = list(map(int, input().split()))
    indice = T.index(max(T))
    cityWin[indice] +=1


print(cityWin.index(max(cityWin))+1)
