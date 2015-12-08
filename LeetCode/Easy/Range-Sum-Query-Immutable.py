class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum = 0
        self.nums =
        # self.nums = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        

        '''
        if i == j-1:
            self.sum += self.nums[i] + self.nums[j]
            return self.sum
        elif i == j:
            self.sum += self.nums[i]
            return self.sum
        else:
            self.sum += self.nums[i] + self.nums[j]
            return self.sumRange(i+1, j-1)
        '''

numArray = NumArray([-2,0,3,-5,2,-1])
print(numArray.sumRange(2, 5))

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)