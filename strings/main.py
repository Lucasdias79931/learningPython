
def strStr(haystack: str, needle: str) -> int:
        if not needle or not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1

        sizeNeedle = len(needle)
        
        end = sizeNeedle 
        
        for start in range(len(haystack)):
            
            word = haystack[start:end]
            print(end)
            if word == needle:
                return start
            
            end +=1
        return -1
            
def isPalindrome(s:str)->bool:
    return s == s[::-1]



class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        longest_pali = ""

        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if self.isPalindrome(word) and len(word) > len(longest_pali):
                    longest_pali = word

        return longest_pali if longest_pali else s[0]  


