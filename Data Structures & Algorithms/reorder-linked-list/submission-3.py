# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Traverse through to the middle of the list (using slow and fast pointers)
        # reverse the second half of the linked list
        # Go through the two list and alternate them while inserting (using even/odd)
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now the slow pointer is pointing to the middle of the list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # now the prev is pointing to the start of the second list
        secondHead = prev
        dummy = ListNode(None)
        curr = dummy
      
        count = 0
        while head and secondHead:
            if count % 2 == 0:
                curr.next = head
                head = head.next
            else:
                curr.next = secondHead
                secondHead = secondHead.next
            count += 1
            curr = curr.next




