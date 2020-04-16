# 120. Triangle
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle : return []
        if len(triangle)==1: return min(triangle[0]);

        trianglelen = len(triangle) 
        for i in range(len(triangle)-1):
            t1 = triangle[i];
            t2 = triangle[i+1];
            t2[0] += t1[0]
            l = len(t1)
            for j in range(1, l):
                t2[j] += min(t1[j-1], t1[j])
            t2[l] += t1[l-1]
        return min(triangle[trianglelen-1])
        