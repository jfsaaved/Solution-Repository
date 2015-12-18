# Author: Julian Saavedra
# GitHub: jfsaaved


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        final_string = ''
        while s:
            index = min(map(s.rindex, set(s)))
            letter = min(s[:index+1])
            final_string += letter
            s = s[s.index(letter):].replace(letter, '')
        return final_string

sol = Solution()
print(sol.removeDuplicateLetters("caccabad"))
print(sol.removeDuplicateLetters("cbacdcbc"))
print(sol.removeDuplicateLetters("abcac"))
print(sol.removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
