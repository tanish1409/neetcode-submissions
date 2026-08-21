# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
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

        if len(lists) == 1:
            return lists[0]

        for lst in range(len(lists) - 1):
            list1 = lists[lst]
            list2 = lists[lst + 1]
            curr1 = list1
            curr2 = list2

            dummy = ListNode(0)
            curr = dummy

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
            
            lists[lst+1] = dummy.next
        
        return lists[-1]

