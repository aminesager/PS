def canEatAll(piles, k, h):
    c = 0 
    for pile in piles:
        c += (pile + k-1) // k
    return c <= h
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        i, j = 1, max(piles)
        mink = j
        while i < j:
            mid = (i + j) // 2
            if canEatAll(piles, mid, h):
                j = mid-1
                mink = min(mink, mid)


            else:
                i = mid+1
            
            
        return mink


sol = Solution()
print(sol.minEatingSpeed([30,11,23,4,20], 5))  