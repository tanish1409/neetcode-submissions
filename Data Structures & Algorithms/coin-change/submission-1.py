class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt in cache:
                return cache[amt]
            res = 1e9
            for c in coins:
                if amt - c >= 0:
                    res = min(res, 1+dfs(amt-c))
                    cache[amt] = res
            return res                    
        minCoin = dfs(amount)

        return -1 if minCoin >= 1e9 else minCoin