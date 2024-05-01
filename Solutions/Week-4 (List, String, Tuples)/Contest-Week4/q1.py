"""Q1. Create a python function named 
isPalindrome which accepts a string as a 
parameter and return True if its a palindrome. 
Palindrome are words which is same when read from start and same 
when read from the end."""


def isPalindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]


print(isPalindrome(s="ABCcbaa"))
