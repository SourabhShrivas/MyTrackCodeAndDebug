"""https://www.naukri.com/code360/problems/check-palindrome-recursive_624386"""


def isPalindrome(str: str, i) -> bool:
    if i >= len(str) // 2:
        return True
    if str[i] != str[len(str) - i - 1]:  # str[len(str) - i - 1] is similar to str [-1]
        return False
    return isPalindrome(str, i + 1)


print(isPalindrome("racecar", 0))
