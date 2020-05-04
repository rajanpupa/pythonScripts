
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not len(inorder): return None;
        if len(inorder) == 1 : return TreeNode(inorder[0]);

        size = len(postorder);
        rootelem = postorder.pop(size-1);
        root = TreeNode(rootelem)

        ind = inorder.index(rootelem);
        # left subtree
        root.left = self.buildTree(inorder[:ind], postorder[:ind])

        # right subtree
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:])

        return root;



# Solution:
# postorder -> left, right, root
# inorder  -> left, root, right
# so the last element in the postorder is always the root element of the current tree/subtree
# find the element in the inorder. all the elements on the left are the inorder elements on the left
#   all the elements on the right of that are the inorder elements on the right
#   the count of the elements in the inorder and preorder for the left subtree and right subtree are same 
    