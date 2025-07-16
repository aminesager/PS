from math import sqrt
for _ in range(int(input())):
    h1, w1, h2, w2, h3, w3 = map(int, input().split())
    
    tot = h1*w1 + h2*w2 + h3*w3     
    side = round(sqrt(tot))
    answer=""

    if h1 == h2 == h3 == side and w1 + w2 + w3 == side:
        answer = ('Yes')
        
    if w1 == w2 == w3 == side and h1 + h2 + h3 == side:
        answer = ('Yes')
        
    if h1 + h2 == side and w1 == w2 and w1 + w3 == side and h3 == side:
        answer = ('Yes')

    if w1 + w2 == side and h1 == h2 and h1 + h3 == side and w3 == side:
        answer = ('Yes')

    if (h1 == side and w2 == side - w1 and w3 == side - w1 and h2 + h3 == side):
        answer = ('Yes')
    if (w1 == side and h2 == side - h1 and h3 == side - h1 and w2 + w3 == side):
        answer = ('Yes')
    
    if answer == 'Yes':
        print('Yes')
    else:
        print('NO')