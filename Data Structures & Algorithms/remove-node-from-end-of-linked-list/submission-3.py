# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse through the entire list to know how many nodes there are - calculate it, and traverse again two passes of O(n) remove the third (using prev pointer)
        # Another method is to use two pointers, let the fast pointer have a head start of n, and slow will be pointing at the nth node from the end by the time fast pointer is at the end 

        '''
        [5]
         s f
        n=1

        '''
     
        first = head
        count = 0
        while count < n:
            first = first.next
            count += 1

    
        dummy = ListNode(None)
        dummy.next = head
        
        second = head
        prev = dummy
        prev.next = second
        while first:
            prev = second
            second = second.next
            first = first.next
        
        prev.next = second.next
        return dummy.next

            