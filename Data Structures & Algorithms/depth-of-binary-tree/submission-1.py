# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd = 0

        if root is None:
            return 0
        
        st =[[root,1]]
        while st:
            node, height = st.pop()  

            if node:
                maxd = max(maxd, height)
                st.append([node.left,height +1])
                st.append([node.right, height +1])
        return maxd
                