class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(t)):
            c1[ord(s[i]) - ord('a')] += 1
            c2[ord(t[i]) - ord('a')] += 1
        

        for i in range(26):
            if c1[i] != c2[i]:
                return False

        return True
