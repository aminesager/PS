s= input()
x,y,z = s[0],s[1],s[2]


t=[x,y,z]

t.sort(key=lambda x:x[0], reverse=True)

print(t)