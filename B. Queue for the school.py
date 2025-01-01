def swap(T, a, b):
    aux = T[a]
    T[a] = T[b]
    T[b] = aux
    return T
#----------------------------------------------------------------  
a = input()
n= int(a[0:a.find(' ')])
t = int(a[a.find(' ') + 1:])
#----------------------------------------------------------------  

s = input()

T = list(s)


for x in range(t):
    i = 0
    while i < len(T) - 1:
        if T[i]< T[i + 1]:
            swap(T, i, i + 1)
            i=i+2
        else:
            i=i+1


s = ""
for i in range(len(T)):
    s=s+T[i]
    
print(s)