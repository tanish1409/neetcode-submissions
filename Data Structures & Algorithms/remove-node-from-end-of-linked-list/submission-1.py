# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next

        rem = count-n

        curr = dummy
        while curr and rem > 0:
            curr = curr.next
            rem -=1

        curr.next = curr.next.next

        return dummy.next

       
    
        