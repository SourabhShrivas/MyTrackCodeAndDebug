"""'https://leetcode.com/problems/palindrome-number/description/"""


class Solution:
    def isPalindrome(self, x: int):
        number = x
        if number < 0:
            return False

        reverse_number = 0
        # print(x)

        while number > 0:
            last_digit = number % 10
            reverse_number = reverse_number * 10 + last_digit
            number = number // 10
        print(reverse_number)

        if reverse_number == x:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome(121))
