# 117. Populating Next Right Pointers in Each Node II
# Same as question 116, but the tree is not perfectly balanced
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root;
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            prev = None
            for i in range(size):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
                if prev:
                    prev.next = n
                # update prev only if n is not None
                if n:
                    prev = n
        return root  