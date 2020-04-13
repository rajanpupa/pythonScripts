# We are given N different types of stickers. Each sticker has a lowercase English word on it.
# You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.
# You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
# What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.
# Example 1:
# Input:
# ["with", "example", "science"], "thehat"
# Output:
# 3
# Example 2:
# Input:
# ["notice", "possible"], "basicbasic"
# Output:
# -1

# Solution copied
from collections import Counter, defaultdict
from math import inf, isinf

class Solution:
    def minStickers(self, stickers, target: str) -> int:
        s_cnts = *map(Counter, stickers),
        dp = defaultdict(lambda: inf, {(): 0})
        def helper(cnt):
            _id = tuple(cnt.items())
            if isinf(dp[_id]):
                dp[_id] = 1 + min((helper(cnt - s_cnt) for s_cnt in s_cnts if s_cnt[_id[0][0]]), default=inf)
            return dp[_id]
        return -1 if isinf(ans := helper(Counter(target))) else ans





s = Solution()
stickers = ["with", "example", "science"]
target = "thehat"
s.minStickers(stickers, target);