while True:
    n = int(input("Enter a number: "))
    if n in range(1, 100):
        break
if n%2 == 0 and n > 2 :
    print("Yes")
else:
    print("No")