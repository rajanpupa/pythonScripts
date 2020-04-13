# 113. Path Sum II
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isleaf(self, root) -> bool:
        if not root: return False;
        return not root.left and not root.right;
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        lst = []
        if self.isleaf(root) :
            if root.val == sum:
                lst.append([root.val]);
            return lst;
        
        stk = []
        stk.append(root);
        while stk:
            elem = stk.pop()
            if elem:
                