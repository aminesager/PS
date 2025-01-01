t= int(input())
while(t):
    t = t -1   
    line = input("")
    n, k = map(int, line.split())
    s = input("")
    T = [int(num) for num in s.split()]
    s = 0
    T.remove(max(T))
    for i in range(len(T)):
        s=s+T[i]
        if T[i] == 2 :
            s += 1
        else:
            s = s+(T[i]) -1
    print(s)