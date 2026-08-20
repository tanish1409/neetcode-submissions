class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        max_val = max(interval[0] for interval in intervals)
        res = []

        mp = [0] * (max_val+1)

        cover = -1
        int_start = -1

        for start,end in intervals:
            mp[start] = max(end + 1, mp[start])

        for i in range(len(mp)):
            if mp[i] != 0:
                if int_start == -1:
                    int_start = i
                cover = max(mp[i]-1, cover)
                
            if cover == i:
                res.append([int_start,cover])
                have = -1
                int_start = -1

        if int_start != -1:
            res.append([int_start, cover])
        return res
        