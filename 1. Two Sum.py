def twoSum(nums, target):
    l = 0
    cp = nums 
    r = len(nums)-1
    nums.sort()
    output = [0,0]
    while l < r:
        if nums[l] + nums[r] == target:
            break
        
        elif nums[l] + nums[r] > target:
            r -= 1
        
        else:
            l += 1
    output[0] = cp.index(nums[l])
    output[1] = len(cp) - 1 - cp[::-1].index((nums[r]))
    return output


print(twoSum([3,2,4], 6))       
         