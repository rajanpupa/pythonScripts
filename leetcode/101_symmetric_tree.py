# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        elemlr = self.dfs(root, True)
        elemrl = self.dfs(root, False)
        return elemrl == elemlr
    
    def dfs(self, root: TreeNode, lr: bool) -> List:
        bfs = []
        bfs.append(root)
        elem = []
        while len(bfs):
            node = bfs.pop(0)
            if node:
                elem.append(node.val)
                if lr:
                    bfs.append(node.left)
                    bfs.append(node.right)
                else:
                    bfs.append(node.right)
                    bfs.append(node.left)
            else:
                elem.append(None)
        return elem    


        
      
            
            
            
            
            
            
            