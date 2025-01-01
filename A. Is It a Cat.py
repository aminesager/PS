t = int(input())
while(t):
    t = t - 1
    n = int(input())
    s=input().upper()
    c=""
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            c=c+s[i]
    c=c+s[len(s)-1]       
    if c=='MEOW':
        print("YES")
    else:
        print("NO")