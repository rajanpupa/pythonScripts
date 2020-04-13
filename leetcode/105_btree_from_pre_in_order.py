# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # print("preorder", preorder)
        # print("inorder", inorder)
        # print("---------------------------------")
        if not len(inorder) : return None;
        if len(inorder) == 1:
            return TreeNode(inorder[0]);
        
        rootelem = preorder.pop(0);
        i = inorder.index(rootelem)
        
        # create the root node for this traversal
        root = TreeNode(rootelem);
        root.left = self.buildTree(preorder[:i-1], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])
        return root;
# Solution:
# preorder -> root, left, right
# inorder  -> left, root, right
# so the first element in the preorder is always the root element of the tree
# find the element in the inorder. all the elements on the left are the inorder elements on the left
#   all the elements on the right of that are the inorder elements on the right
#   the count of the elements in the inorder and preorder for the left subtree and right subtree are same 
    