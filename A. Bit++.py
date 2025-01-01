n = int(input(""))
X = 0
while(n):
    n = n - 1
    s = input("")
    if "++" in s:
        X += 1
    if  "--" in s:
        X -= 1
print(X)
