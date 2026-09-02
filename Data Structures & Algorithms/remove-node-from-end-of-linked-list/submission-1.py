# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate through the list until the prev pointer is one before n (n-1) because I will set the prev pointer.next
        # to the node after n
        # wait, from the end of the list
        # it is NOT 0th index 
       
        # Simple way is to iterate through the entire list once to find out how many nodes there are and do math to figure out
        # what position is the nth node from the end
        # But you can also use two pointers, one of the pointers will have a head start, incrementing by n
        # Once the pointer is at the nth spot, start another pointer at the head and now iterate though the list such that it stops when
        # the first pointer is at the end (the second pointer will be pointing at the node to be skipped)

        # First I'll do the simpler way of iterating through it twice
  

    #     curr = head
    #     length = 0
        
    #     while curr:
    #         length += 1
    #         curr = curr.next
    # # At the end of this loop, you will know the length
    # # Use this length number to calculate what node from 0 to remove
    #     removalIndex = length - n

    #     dummy = ListNode() #I'm using a dummy node incase i need to remove the starting node and it ensures I can still be pointing at the correct head
    #     dummy.next = head

    #     prev = dummy
    #     curr = head
    #     index = 0
    #     # now iterate through the list a second time, this time to remove the removalIndex node
    #     curr = head
    #     while curr:
    #         if index == removalIndex:
    #             prev.next = curr.next
    #             return dummy.next
    #         index += 1
    #         prev = curr
    #         curr = curr.next
    #     return dummy.next


# Now I'll do the more efficient way of iterating through it twice
  

        end = head
        length = 0
        
        while length != n:
            length += 1
            end = end.next
    # At the end of this loop you will be nth node in, now start another pointer starting at the head
    # Do the deletion here as well

        dummy = ListNode() #I'm using a dummy node incase i need to remove the starting node and it ensures I can still be pointing at the correct head
        dummy.next = head

        prev = dummy
        curr = head
        nxt = None
        while end:
       
            end = end.next
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
           

        # now iterate through the list a second time, this time to remove the removalIndex node

    
        return dummy.next
          







