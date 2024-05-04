"""https://leetcode.com/problems/reverse-integer/description/

"""


class Solution:
    def reverse(self, x: int) -> int:
        n = x
        reverse_num = 0
        is_negative = 1

        if n < 0:
            is_negative = -1
            n = abs(n)

        while n > 0:
            last_digit = n % 10
            reverse_num = reverse_num * 10 + last_digit
            n = n // 10

        reverse_num = reverse_num * is_negative

        if reverse_num < (-(2**31)) or reverse_num > (2**31 - 1):
            return 0

        return reverse_num


a = Solution()
print(a.reverse(2345))
