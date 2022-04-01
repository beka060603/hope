list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Solution:
    def plusOne(digits: list) -> list:
        list[-1] = list[-1] + 1

    print(list)


Solution.plusOne(list)

while 1:
    x = input()
    if x == x[::-1]:
        print(True)
    else:
        print(False)
