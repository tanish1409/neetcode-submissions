# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # if not root:
        #     return None
        
        # st = [(root)]
        # arr = []
        # while st:
        #     node = st.pop()
        #     arr.append(node.val)
        #     if node.left:
        #         st.append(node.left)
        #     if node.right:
        #         st.append(node.right)

        # arr.sort()

        # return arr[k-1]

        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
        
            curr = st.pop()
            k -= 1

            if k==0:
                return curr.val

            curr= curr.right
        