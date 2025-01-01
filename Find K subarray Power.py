tab = list(map(int, input().split()))
k = int(input())


isSorted = True
Arr = []
c = 1
for i in range(1,len(tab)):

    if tab[i] - tab[i-1] != 1:
        c=1
        isSorted = False
    else:
        c += 1
    
    if not isSorted :
        if c>= k:
            isSorted= True
        else:
            if i>= k-1:
                Arr.append(-1)
            
    if isSorted and c >= k:
        Arr.append(tab[i])
 
print(Arr)  