def get_list() -> list:
    return list(range(0, 10000000, 2))


"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:

    def find_target(self, list, target):
        lower_b = 0
        upper_b = len(list)
        pop = 0
        while lower_b < upper_b:
            pop += 1
            centr = (lower_b + upper_b) // 2
            if list[centr] == target:
                return pop, target
            elif list[centr] > target:
                upper_b = centr - 1
            elif list[centr] < target:
                lower_b = centr + 1
        return -1


p = Solution().find_target(get_list(), 500)
print(p)
import random
from typing import Union, List

#
# class Arrays:
#     def __init__(self):
#         self.nesting = random.randint(50, 150)
#         self.arrays = self.get_array(1)
#
#     def get_array(self, step) -> Union[List[list], int]:
#         if step <= self.nesting:
#             return [self.get_array(step + 1)]
#         else:
#             return random.randint(1_000, 100_000)
#
#
# nested_arrays = Arrays()
#
#
# class Solution:
#
#     def get_num(self, arrays: list) -> int:
#
#
# Solution().get_num(nested_arrays.arrays)
