class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        new_count = 0

        for i in nums:
            if i == 1:
                new_count += 1
                count = max(count, new_count)
            else:
                new_count = 0
                
        return count