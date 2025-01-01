t = int(input(""))
while(t):
    t = t - 1
    n = int(input(""))
    s = input()
    c=""

    if (s.count("1") > (s.count("0"))):
        print("Yes")

    else:
        for i in range(len(s)-1):
            if s[i] == '1':
                c=c+s[i]
            elif s[i] != s[i+1]:
                c=c+s[i]
        c=c+s[len(s)-1]

        if (c.count('1')> c.count('0')):
            print('YES')
        else:
            print('NO')