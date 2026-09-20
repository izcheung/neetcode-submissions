"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        seen = {}
        # Create all the nodes first
        while curr:
            newNode = Node(curr.val)
            seen[curr] = newNode
            curr = curr.next
        
        newCurr = head
        dummy = Node(0)


        copyCurr = seen[newCurr]
        dummy.next = copyCurr

        while newCurr:
            if newCurr.next:
                copyCurr.next = seen[newCurr.next]
            if newCurr.random:
                copyCurr.random = seen[newCurr.random]
            newCurr = newCurr.next
            copyCurr = copyCurr.next
    
        return dummy.next

