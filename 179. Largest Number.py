
def largestNumber(nums):
    
    num_strings = [str(num) for num in nums]
    num_strings.sort(key=lambda a: a * 10, reverse=True)
    if num_strings[0] == "0":
        return "0"

    return "".join(num_strings)



nums = [3332,30,34,5,9]

print(largestNumber(nums))