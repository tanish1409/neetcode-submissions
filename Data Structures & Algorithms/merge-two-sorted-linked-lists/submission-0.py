# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        ret = retList = ListNode()

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                retList.next = curr1
                curr1 = curr1.next
            else:
                retList.next = curr2
                curr2 = curr2.next
            retList = retList.next

        if curr1:
            retList.next = curr1
        else:
            retList.next = curr2

        return ret.next
                
        