# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Check if the node is leaf node or not.
class Solution:
    def isleaf(self, root) -> bool:
        if not root: return False;
        return not root.left and not root.right;
    
    def hps(self, root, sum) -> bool:
        if not root: return False;
        if self.isleaf(root):
            if root.val == sum: return True;
            return False;
        
        return self.hps(root.left, sum - root.val) or self.hps(root.right, sum - root.val);
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False;
        return self.hps(root, sum);