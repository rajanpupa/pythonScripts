# 114. Flatten Binary Tree to Linked List
# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root : return
        
        right = root.right
        root.right = root.left
        root.left = None
        
        temp = root
        while temp.right: temp=temp.right
        temp.right = right
        self.flatten(root.right)
        