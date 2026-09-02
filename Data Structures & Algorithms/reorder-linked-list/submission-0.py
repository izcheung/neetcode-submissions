# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the second half of the linked list
        # Use a fast and slow pointer to find out where the halfway point is
        # Once you are at the halfway point (slow pointer), then start reversing
      

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow should be at the halfway point
        # Reverse the linked list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is now pointing to the new head (the last node)

       
        dummy = ListNode(None)
        dummy.next = head

        curr1 = head
        curr2 = prev
        while curr2.next:
            currNxt = curr1.next 
            curr2Nxt = curr2.next
          
            curr1.next = curr2
            curr2.next = currNxt
            curr1 = currNxt
            curr2 = curr2Nxt


