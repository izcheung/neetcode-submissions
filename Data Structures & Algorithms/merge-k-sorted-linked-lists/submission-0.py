# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Find out how many linked lists are in the array
        result = []
    
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                result.append(curr.val)
                curr = curr.next
        result.sort()


        dummy = ListNode()
        curr = dummy
        for num in result:
            newNode = ListNode(num)
            dummy.next = newNode
            dummy = dummy.next
        return curr.next

        
