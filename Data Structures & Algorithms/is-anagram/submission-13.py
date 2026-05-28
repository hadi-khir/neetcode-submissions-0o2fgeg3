class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sMap = {}
        tMap = {}

        for c in s:
            if c in sMap:
                sMap[c] = sMap.get(c) + 1
            else:
                sMap[c] = 1
        
        for c in t:
            if c in tMap:
                tMap[c] = tMap.get(c) + 1
            else:
                tMap[c] = 1
    
        return tMap == sMap