class Solution(object):
    def twoSum(self, List, target):
        l=0
        r=len(List)-1
        cp = list(List)

        List.sort()
        while(l<r) and List[l]+List[r] != target:
            if (List[l]+List[r]) > target:
                r-=1
            elif List[l]+List[r] < target:
                l+=1
        
        val1 = List[l]
        val2 = List[r]
        index1 = cp.index(val1)
        
        index2 = cp.index(val2)
        return [index1, index2]
    
    
solution = Solution()

List = [3,2,4]
target = 6
result = solution.twoSum(List, target)
print(f"The indices of the two numbers that add up to {target} are: {result}")