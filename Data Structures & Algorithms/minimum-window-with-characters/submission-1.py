class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return""
        
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        need_count = len(need)
        have = 0
        left = 0

        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have +=1

            while need_count == have:
                curr_len = right - left + 1
                if curr_len < best_len:
                    best_start = left
                    best_len = curr_len

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -=1

                left +=1

        if best_len == float("inf"):
            return ""

        return s[best_start: best_start + best_len]


        