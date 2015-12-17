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

            smallest_item = {}
            temp = lowest
            for item in to_add_list:
                if item not in final_list and item not in smallest_item:
                    smallest_item.update({item: temp})
                temp += 1

            test = False
            if smallest_item:
                test = True

            print("list: {} and map: {} status: {}".format(to_add_list, smallest_item, test))
            priority_element = s[ceilings[index]]
            if not smallest_item:
                lowest = ceilings[index]
            else:
                add_this = priority_element
                smaller_element = min(smallest_item)
                if smaller_element not in final_list:
                    if smaller_element < add_this:
                        add_this = smaller_element

                if isinstance(smallest_item.get(add_this), int):
                    lowest = smallest_item.get(add_this) + 1
                    final_list.append(add_this)
                    print(add_this)
                else:
                    print("not able to add: {}".format(smallest_item.get(add_this)))

            if priority_element in final_list:
                index += 1

        final_string = ""
        for item in final_list:
            final_string += item

        return final_string

sol = Solution()
print(sol.removeDuplicateLetters("caccabad"))
print("------------------------------------")
print(sol.removeDuplicateLetters("cbacdcbc"))
print("------------------------------------")
print(sol.removeDuplicateLetters("abcac"))
print("------------------------------------")
print(sol.removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk"))
