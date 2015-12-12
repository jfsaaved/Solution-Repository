"""
Author: Julian Saavedra
GitHub: jfsaaved
"""


class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0

        secret_map = {}

        for secret_item in secret:
            if secret_item not in secret_map:
                secret_map[secret_item] = 1
            elif secret_item in secret_map:
                secret_map[secret_item] += 1

        index = 0
        guess_cow_list = []
        for secret_item in secret:
            if secret_item == guess[index]:
                bull += 1
                secret_map[guess[index]] -= 1
            else:
                guess_cow_list.append(guess[index])
            index += 1

        for guess_item in guess_cow_list:
            if guess_item in secret_map and secret_map[guess_item] > 0:
                cow += 1
                secret_map[guess_item] -= 1

        return "{}A{}B".format(bull, cow)

test = Solution()
print(test.getHint('1', '0'))
print(test.getHint('1122', '2211'))
print(test.getHint('1234', '0111'))
