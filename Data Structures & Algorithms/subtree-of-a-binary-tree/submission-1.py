# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot): 
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        st = [(root, subRoot)]

        while st:
            node1 , node2 = st.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            st.append((node1.left,node2.left))
            st.append((node1.right,node2.right))
        return True
    


        