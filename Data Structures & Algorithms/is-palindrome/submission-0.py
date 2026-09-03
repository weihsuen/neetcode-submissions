class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedstring = ""
        
        #remove nonalphabet
        for c in s:
            if c.isalnum():
                cleanedstring += c.lower()

        return cleanedstring == cleanedstring[::-1]