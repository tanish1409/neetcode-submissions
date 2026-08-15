# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        print(arr) 
       
        rem = len(arr) - n
        arr.pop(rem)
        if not arr:
            return None

        retList = ListNode
        curr = retList
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next

        return retList.next
        
        