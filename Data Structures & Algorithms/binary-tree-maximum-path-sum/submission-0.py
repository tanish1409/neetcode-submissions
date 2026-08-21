# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def findMax(node: Optional[TreeNode]) -> int:
            
            if not node:
                return 0

            left_gain = max(0, findMax(node.left))
            right_gain = max(0,findMax(node.right))

            return node.val + max(left_gain, right_gain)

        def traverse(node: Optional[TreeNode]):

            if not node:
                return

            left_best = max(0, findMax(node.left))
            right_best = max(0, findMax(node.right))

            curr_best = node.val + left_best + right_best

            self.res = max (self.res, curr_best)

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return self.res


        