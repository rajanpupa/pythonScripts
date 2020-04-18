# Circular loop detection:
# Given a circular linkedl list, return the first node in the circle
# A->B->C->D->E->c
# return: C
class Node:
    c = 0
    n = 0
    def __init__(self, val):
        self.val = val
        self.next = None
        Node.n += 1
    def __str__(self):
        Node.c += 1
        s = "- > " + str(self.val)
        if self.next and Node.c <= Node.n:
            s += str(self.next)
        return s;

class Solution:
    def curcular_head(self, head: Node) -> int:
        if not head or not head.next: return head;
        l1 = head
        l2 = head.next
        while l2.val != l1.val:
            l2 = l2.next
            if(l1.val==l2.val): break
            l2 = l2.next
            if(l1.val==l2.val): break
            l1 = l1.next
            if(l1.val==l2.val): break
        return l2.val;

def make_circular_list( arr )->Node:
    head = Node(arr[0])
    p = head
    d = {}
    d[arr[0]] = head
    for i in range( 1, len(arr) ):
        if arr[i] in d:
            p.next = d.get(arr[i])
            return head
        else:
            nxt = Node(arr[i])
            d[arr[i]] = nxt
            p.next = nxt
            p = nxt
    return head

head = make_circular_list([1,2,3,4,5,6,1])

print(Node.c)

print(head)
s = Solution()
print(s.curcular_head(head));
