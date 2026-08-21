class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        visit = set()
        res = 0

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):

            if node in visit:
                return

            visit.add(node)

            for neigh in adj[node]:
                dfs(neigh)


        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res
            
        
        