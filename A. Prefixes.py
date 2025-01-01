n = int(input())
s = input()
T= list(s)


res=0

def pair(T,i):
    global res
    if T[i] + T[i+1] not in ['ab', 'ba']:
        res = res +1
        if T[i] == 'a':
            T[i+1] ='b'
        else:
            T[i+1] = 'a'

for i in range(0,n-1,2):
    pair(T,i)
    

s = ""
for i in range(len(T)):
    s=s+T[i]
print(res)
print(s)






