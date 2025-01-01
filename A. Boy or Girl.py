s=input()
T=[]

c = 0
for i in range(len(s)):
    if s[i] not in T:
        T.append(s[i])
        c+=1

if c % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")