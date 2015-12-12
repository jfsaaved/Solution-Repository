"""
Author: Julian Saavedra
GitHub: jfsaaved
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_map = {}
        str_list = str.split()
        pattern_list = []
        i = 0

        if len(pattern) == len(str_list):
            for letter in pattern:
                if letter not in str_map:
                    if str_list[i] in str_map.values():
                        return False
                    else:
                        str_map.update({letter : str_list[i]})
                i += 1
        else:
            return False

        for letter in pattern:
            if letter in str_map:
                pattern_list.append(str_map.get(letter))

        if str_list == pattern_list:
            return True
        else:
            return False

sol = Solution()
print(sol.wordPattern("abba","dog cat cat dog"))
print(sol.wordPattern("jquery","jquery"))
print(sol.wordPattern("j","jquery"))