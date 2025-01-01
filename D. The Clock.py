for zebbi in range(int(input())):
    hm, x = map(str, input().split())

    x = int(x)

    h = int(hm[0:2])
    m = int(hm[3:6])

    pal=0

    for i in range(1440 // x):
        m += x
        if m>= 60:
            h += m //60
            m = m % 60
        
        if h>23:
            h = h-24
        
        hours = str(h)
        mins = str(m)
        
        if h<10:
            hours = '0' + hours
        if m<10:
            mins = '0' + mins
        time = hours + mins    
        if time == time[::-1]:
            print(time)
            pal += 1
            
    print(pal)
