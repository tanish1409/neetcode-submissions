class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in hashmap_s: 
                hashmap_s[s[i]] = 0
            hashmap_s[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in hashmap_t: 
                hashmap_t[t[i]] = 0 
            hashmap_t[t[i]] += 1

        if hashmap_s == hashmap_t:
            return True

        else:
            return False
        