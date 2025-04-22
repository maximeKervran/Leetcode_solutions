# Last updated: 22/04/2025 18:20:01
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resString = []
        taille = 0
        for element in s:
            if element in resString:
                if len(resString) > taille:
                    taille = len(resString)
                index = resString.index(element)
                resString = resString[index + 1:]
                resString.append(element)
            else:
                resString.append(element)
        if len(resString) > taille:
            taille = len(resString)
        return taille
