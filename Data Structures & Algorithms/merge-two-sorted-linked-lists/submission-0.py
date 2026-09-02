# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # have a pointer pointing to the start of each list
    # list1=[1,2,4]
    # list2=[1,3,5]

        l1 = list1
        l2 = list2
        newList = ListNode(None)
        tail = newList
        while l1 and l2:
            if l1.val <= l2.val:
                newList.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        if l1:
            newList.next = l1
        if l2:
            newList.next = l2

        return tail.next