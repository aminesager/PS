def ORbitwise(x, y):
    bin1 = bin(x)[2:]
    bin2 = bin(y)[2:]
    diff = abs (len(bin1) - len(bin2))
    if len(bin1) > len(bin2):
        bin2 = "0"* diff + bin2
    else:
        bin1 = "0"* diff + bin1
    ORsum = ""
    for i in range(len(bin1)):
        if bin1[i] + bin2[i] == "00":
            ORsum = ORsum + "0"
        else:
            ORsum = ORsum + "1"       
    return (bin(int(ORsum,2)))

def sequence(n):
    T = list(range(0, n + 1))
    Arr = []
    for v in range(1, n + 1):
        for x in range(v, n + 1):
            actual = x
            i = v
            while i < n + 1:
                if bin(actual | T[i]) == bin(n):
                    Arr.append(actual)
                    actual = T[i]
                    Arr.append(actual)
                i += 1
    return Arr 
            



def longest(Arr):
    max_len = 0
    max_idx = 0
    cur_len = 1
    cur_idx = 0
    
    for i in range(1, len(Arr)):
        if Arr[i] >= Arr[i - 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                max_idx = cur_idx
            
            cur_len = 1
            cur_idx = i

    if cur_len > max_len:
        max_len = cur_len
        max_idx = cur_idx

    return Arr[max_idx:max_idx + max_len]


t=int(input())
while(t):
    t=t-1
    n = int(input())
    Arr = sequence(n)

    Arr1 = []
    for i in range(len(Arr)-1):
        if Arr[i] != Arr[i+1]:
            Arr1.append(Arr[i])
    Arr1.append(Arr[len(Arr)-1])
    Arr1 = (longest(Arr1))

    result = ' '.join(map(str, Arr1))

    print(len(Arr1))
    print(result)
