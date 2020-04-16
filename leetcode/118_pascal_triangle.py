# 118. Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows < 1: return ans
        ans.append([1])
        for i in range(1,numRows):
            lst = []
            lst.append(1)
            prvlst = ans[i-1]
            for j in range(1,i):
                lst.append(prvlst[j-1]+ prvlst[j])
            lst.append(1)
            ans.append(lst)
        return ans;
