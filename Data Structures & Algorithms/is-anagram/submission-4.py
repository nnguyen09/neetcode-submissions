class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for e in s:
            if e in s1:
                s1[e] += 1
            else:
                s1[e] = 1  
            

        for e in t:
            if e in s2:
                s2[e] += 1
            else:  
                s2[e] = 1

        print(s1)
        print(s2)

        if (s1 == s2):
            return True
        else:
            return False

