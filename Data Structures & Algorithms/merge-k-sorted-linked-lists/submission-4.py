# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  

    def mergeTwo(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]):

            
            dummy = ListNode(0)
            curr = dummy
            curr1 = list1
            curr2 = list2

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next

                curr = curr.next
    

            if curr1:
                curr.next = curr1
            else:
                curr.next = curr2

            return dummy.next
              
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # nodes = []
        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        #         lst = lst.next

        # nodes.sort()

        # dummy = ListNode(0)
        # curr = dummy

        # for n in (nodes):
        #     curr.next = ListNode(n)
        #     curr = curr.next

        # return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeTwo(l1,l2))
            lists = merged_lists

        return lists[0]

