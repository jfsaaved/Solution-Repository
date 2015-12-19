# Author: Julian Saavedra
# GitHub: jfsaaved


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        ugly_numbers = [2, 3, 5]
        for x in ugly_numbers:
            while num % x == 0:
                num = num / x
        return num == 1


sol = Solution()
print(sol.isUgly(4))
print(sol.isUgly(-8))
print(sol.isUgly(-2147483648))