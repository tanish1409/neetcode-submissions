"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        if not node:
            return None
        def clone(node):

            if node in hmap:
                return hmap[node]

            copy = Node(node.val)
            hmap[node] = copy

            for neighbour in node.neighbors:
                copy.neighbors.append(clone(neighbour))
            return copy

        return clone(node)