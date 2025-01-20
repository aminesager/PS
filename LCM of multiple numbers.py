import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result



  
nums = [3332,30,34,5,9]


def largestNumber(nums):
    nb = (lcm_of_list(nums))
    
    for i in range(len(nums)):
        nums[i] = str(nums[i]) * round(nb / len(str(nums[i])))
        
        
    nums.sort()
    return nums



print(largestNumber(nums))