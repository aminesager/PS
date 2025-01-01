n = int(input(""))
total = 0
while(n):
    n = n - 1
    s = input("")
    
    sum = int(s[0])+int(s[2])+int(s[4])
    if sum>1:
        total += 1
print(total)