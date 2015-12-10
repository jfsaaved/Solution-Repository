"""
Author: Julian Saavedra
GitHub: jfsaaved
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zeros_count = nums.count(0)
        index = 0

        while zeros_count > 0:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
                zeros_count -= 1
                index -= 1

            index += 1

        ''' Alternative, not accept in LeetCode because it creates another list(?)
        num_of_zeros = nums.count(0)
        nums = sorted(nums)
        nums = nums[num_of_zeros:] + nums[0:num_of_zeros]
        '''

        print(nums)


sol = Solution()
sol.moveZeroes([0, 0, 1])