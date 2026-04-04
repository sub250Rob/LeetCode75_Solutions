
'''
Docstring for Increasing_Triple_Subsequence

This is my solution for LeetCode 75, Problem #334 (Difficulty: Medium)
'''

class Solution:

    def increasingTriplet(self, nums):

        for i in range(len(nums)):
            if nums[i] < nums[i+1]:
                if nums[i+1] < nums[i +2]:
                    return True
                
        return False
    

sol = Solution()

print(sol.increasingTriplet([5,4,3,2,1]))