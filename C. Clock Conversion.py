 
t = int(input(""))
while(t):
    t = t - 1
    s= input("")
    h = s[0:2]
    hint = int(h)
    if h == "12":
        s = s + ' PM'
    elif h == "00":
        s = '12' +":"+ s[3:5] + ' AM'
    elif h > '12':
        if hint > 21:
            s = str(hint-12) +":"+ s[3:5] + ' PM'
        else:
            s = '0'+str(hint-12) +":"+ s[3:5] + ' PM'
    elif hint in range(1,12):
        s = s + ' AM'
 
    print(s)
