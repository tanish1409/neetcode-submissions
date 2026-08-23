class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        arr = []
        curr = []
        res = float("-inf")

        for num in nums:
            res = max(num,res)
            if num == 0:
                if curr:
                    arr.append(curr)
                    curr = []
            else:
                curr.append(num)

            
        if curr:
            arr.append(curr)
        for sub in arr:
            negs = sum(1 for i in sub if i<0)
            need = negs if negs % 2 == 0 else negs -1
            negs = 0
            prod = 1
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i]<0:
                    negs +=1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -=1
                        j+=1
                if j<=i:
                    res = max(res,prod)

        return res


