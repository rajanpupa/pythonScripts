# 129. Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.
# Example:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# BFS solution
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root : return 0
        if not root.left and not root.right: return root.val
        
        q = deque()
        q.append(root)
        leafs = []
        while q:
            n = len(q)
            for i in range(n):
                r = q.popleft()
                #print("processing ", r.val)
                if r:
                    if not r.left and not r.right:
                        leafs.append(r.val) 
                    val = r.val
                    if r.left:
                        r.left.val = val * 10 + r.left.val
                        q.append(r.left)
                    if r.right:
                        r.right.val = val * 10 + r.right.val
                        q.append(r.right)
        return sum(leafs )
# DFS solution
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sn(root, 0)
    def sn (self, root, sum)->int:
        if not root: return 0
        if not root.left and not root.right: 
            return sum * 10 + root.val
        return self.sn(root.left, 10*sum+root.val ) + self.sn(root.right, 10*sum + root.val)