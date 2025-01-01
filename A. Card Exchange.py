def maxCount(cards):
    C = set(cards)
    maxN = 0
    for num in C:
        numCount = cards.count(num)
        if numCount > maxN:
            maxN = numCount
    return maxN

for _ in range(int(input())):
    n, k = map(int, input().split())
    cards = list(map(int, input().split()))
        

    if maxCount(cards) < k:
        print(n)
    else:
        print(k-1)

    
    

