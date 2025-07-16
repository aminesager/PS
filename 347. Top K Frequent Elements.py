class Solution(object):
    def topKFrequent(self, nums, k):
        uniq = set(nums)

        value_map = {num: 0 for num in uniq}
        for key in value_map:
            value_map[key] = nums.count(key)

        value_map = sorted(value_map.items(), key=lambda x: x[1], reverse=True)

        result=[]
        for i in range(k): 
            result.append(value_map[i][0])

        return result