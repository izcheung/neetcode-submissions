# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer to find where halfway through the list is
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        # head=[2,4,6,8]
                    # s   f
 


        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # after reversing the second half, I will use the previous (which is pointing to the start of the second half)
        while prev.next:
            nxt = head.next
            pnxt = prev.next

            head.next = prev
            prev.next = nxt
            prev = pnxt
            head = nxt


        # reorder the nodes 
