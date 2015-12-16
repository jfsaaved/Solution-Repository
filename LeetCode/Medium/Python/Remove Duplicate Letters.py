# Author: Julian Saavedra
# GitHub: jfsaaved


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        alpha_map = {}
        index = 0
        for c in s:
            alpha_map.update({c: index})
            index += 1

        ceilings = sorted(alpha_map.values())
        index = 0
        lowest = 0
        final_list = []

        while index < len(ceilings):
            to_add_list = list(s[lowest:ceilings[index] + 1])

            get_lowest_item_here = {}
            temp = lowest
            for item in to_add_list:
                if item not in final_list and item not in get_lowest_item_here:
                    get_lowest_item_here.update({item: temp})
                temp += 1

            if not get_lowest_item_here:
                break

            add_this = min(get_lowest_item_here.keys())
            if ceilings[index] == get_lowest_item_here.get(add_this):
                index += 1
            lowest = get_lowest_item_here.get(add_this) + 1

            final_list.append(add_this)

        final_string = ""
        for item in final_list:
            final_string += item

        return final_string

sol = Solution()
print(sol.removeDuplicateLetters("caccabad"))
print("new")
print(sol.removeDuplicateLetters("cbacdcbc"))