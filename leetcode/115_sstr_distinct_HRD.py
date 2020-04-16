# 115. Distinct Subsequences
# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# It's guaranteed the answer fits on a 32-bit signed integer.
# Example 1:
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # print("processing ", s, t)
        if not s: return 0
        if len(s) < len(t): return 0
        if len(t) == 1 : 
            cnt = s.count(t)
            # print("returning count", cnt)
            return cnt

        # sdic = {}
        # while c in s:
        #     sdic[c] = sdic.get(c,0) + 1
        
        # tdic = {}
        # while c in t:
        #     tdic[c] = tdic.get(c,0)+1
        #     if tdic[c] > sdic[c]: return 0
        
        count = 0
        for i in range(len(s)-len(t)+1):
            # print(i)
            if s[i] == t[0]:
                count += self.numDistinct( s[i+1:], t[1:] )
         
        return count;

sln = Solution()
s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
t="bcddceeeebecbc"
count = sln.numDistinct(s, t);
print(count);
