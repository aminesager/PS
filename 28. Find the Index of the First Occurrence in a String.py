class Solution(object):
    
    def strStr(self, haystack, needle):
        
        if needle not in haystack:
            return -1
        else:
            index = -1
            for i in range(max(1,(len(haystack)-len(needle))+1)):
                if needle == haystack[i:len(needle)+i]:
                    index = i
                    break
            return index

