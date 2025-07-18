class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x + 1
            j = len(nums) - 1
            while i < j:
                total = nums[x] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    result.append([nums[x], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return(result)