# 107: Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root : return [];
        
        arrs = []
        q = deque()
        q.append(root);
        
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                cur = q.popleft();
                if cur:
                    arr.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if  len(arr): arrs.insert(0, arr)
        return arrs;    