def palBinary(nb):
    if len(nb) in range (0, 2):
        return True
    else:
        ones = 0
        zeros = 0
        for i in range (0, len(nb)):
            if nb[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        if (ones % 2 == 1 and zeros % 2 == 1 ):
            return False
        return True
            
nb = '1101'
print(palBinary(nb))