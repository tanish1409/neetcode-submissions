class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # adj = {i:[] for i in range(n)}
        # visit = set()
        # res = 0

        # for n1,n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # def dfs(node):

        #     if node in visit:
        #         return

        #     visit.add(node)

        #     for neigh in adj[node]:
        #         dfs(neigh)


        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         res += 1
        # return res

        rank = [1] *n
        par = [i for i in range(n)]

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:

                par[p2] = p1
                rank[p1] +=1
            else:
                par[p1] = p2
                rank[p2] +=1

            return 1

        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)

        return res
            
        
        