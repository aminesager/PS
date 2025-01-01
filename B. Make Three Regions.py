for _ in range(int(input())):    
 
    n = int(input())
    line1 = input()
    line2 = input()
 
    if n<3 :
        print(0)
    
    else:
        
        result = 0
        case = ["x.x...", "x...x.", ".x...x"]
        for i in range(n-2):
            a = line1[i:i+3]
            b = line2[i:i+3]
            if (a+b in case) or (b+a in case):
                result += 1

        print(result)
 
