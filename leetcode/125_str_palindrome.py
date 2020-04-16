# 125. Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# Input: "race a car"
# Output: false
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        s=s.lower()
        while l<=r :
            while l<r and not s[l].isalnum() : l+=1;
            while l<r and not s[r].isalnum() : r-=1;
            if s[l] != s[r] : return False;
            l+=1
            r-=1
        return True   