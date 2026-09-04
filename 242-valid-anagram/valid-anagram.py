class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts, dictt = {}, {}
        for i in s:
            dicts[i]=dicts.get(i,0) + 1
        for i in t:
            dictt[i]=dictt.get(i,0) + 1
        return dicts==dictt        