class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        for i in range(0,len(haystack)):
            if haystack[i:i+n] == needle:
                return i 
        return -1        
        