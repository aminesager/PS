def longestConsecutive( nums):
    nums = sorted(set(nums))
    longest_streak = 0
    current_streak = 1
    
    
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            current_streak += 1
        if longest_streak < current_streak:
            longest_streak = current_streak
        elif nums[i+1] - nums[i] != 1:
            current_streak = 1
                    
    return longest_streak
        