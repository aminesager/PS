def notReally(s):
    killers = ["11", "-11", "1-1", "-1-1"]
    if len(s)>1:
        for killer in killers:
            if killer in s:
                return True
    return False
 
for _ in range(int(input())):
    #x = int(input())
    #binary = bin(x)[2:]
    binary = '11011011'
    
    if notReally(binary):
        result = []
        count = 0
        count0 = 0
        
        for char in binary:
            if char == '1':
                count += 1
            else:
                if count > 0:
                    result.append('1' * count)
                    count = 0
            if char == '0':
                count0 += 1
            else:
                if count0 > 0:
                    result.append('0' * count0)
                    count0 = 0
                    
        if count > 0:
            result.append('1' * count)
        if count0 > 0:
            result.append('0' * count0)
        
        c = 0
        
        output = ""
        for item in result:
            if item[0] == "1":
                output += ('1'+(len(item)-1)*'0'+'-1')
                c += len(item)+1
            else:
                output += (item)
                c+= len(item)
        
        
        print(c)
        line=(" ".join(output).replace("- ","-"))
    else:
        print(len(bin(x)[2:]))
        line =(" ".join(bin(x)[2:]))
        
    lista = list(map(int, line.split()))
    print(*(lista))
    print(binary)