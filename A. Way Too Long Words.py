n = int(input(""))

while(n):
    n = n - 1
    s = input("")
    if len(s) > 10:
        a = s[0]+str((len(s))-2)+s[len(s)-1]
        print(a)
    else:
        print(s)