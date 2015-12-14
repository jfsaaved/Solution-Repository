# Author: Julian Saavedra
# GitHub: jfsaaved

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        top = n
        bottom = 1
        while True:

            if n == 1:
                return 1
            if n == 2 and isBadVersion(1):
                return 1
            if isBadVersion(n) and isBadVersion(n - 1) == False:
                return n

            if isBadVersion(n):
                top = n
                if (n % 2 != 0 and bottom % 2 == 0) or (n % 2 == 0 and bottom % 2 != 0):
                    n = int((n+bottom) / 2) + 1
                else:
                    n = int((n+bottom)/2)

            elif not isBadVersion(n):
                bottom = n
                if (n % 2 != 0 and top % 2 == 0) or (n % 2 == 0 and top % 2 != 0):
                    n = int((n+top) / 2) + 1
                else:
                    n = int((n+top)/2)


def isBadVersion(num):
    if num >= 500000:
        return True
    else:
        return False

sol = Solution()
print(sol.firstBadVersion(1000000))
