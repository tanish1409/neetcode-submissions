# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        newcurr = dummy

        for val in reversed(arr):
            newcurr.next = ListNode(val)
            newcurr = newcurr.next
            
        return dummy.next
        