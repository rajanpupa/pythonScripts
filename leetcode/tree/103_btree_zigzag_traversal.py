# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        bfs = deque()
        bfs.append(root)
        lst = []
        rtol = True
        while len(bfs):
            l = len(bfs)
            newarr = []
            for i in range(l):
                node = bfs.popleft()
                if node:
                    newarr.append(node.val)
                    bfs.append(node.left)
                    bfs.append(node.right)
            if len(newarr): 
                if rtol:
                    lst.append(newarr)
                else :
                    newarr.reverse()
                    lst.append(newarr)
            rtol = not rtol       
        return lst