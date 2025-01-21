class Solution:
    def twoSum(self, List, target):
        l = 0
        r = len(List)-1

        while(l<r):
            if List[r] + List[l] == target:
                return [l+1, r+1]
            elif List[r] + List[l] > target:
                r-=1
            else:
                l+=1
        return 0
    
    
sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9)) # expected output: [1, 2]