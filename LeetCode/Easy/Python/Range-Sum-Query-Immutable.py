class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum = []

        i = 0
        for num in nums:
            if i == 0:
                self.sum.append(num)
            else:
                self.sum.append(self.sum[i-1] + num)

            i += 1

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sum[j]
        else:
            return self.sum[j] - self.sum[i-1]



numArray = NumArray([-2,0,3,-5,2,-1])
print(numArray.sumRange(0, 2))
