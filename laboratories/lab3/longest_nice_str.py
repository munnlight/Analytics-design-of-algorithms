class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2 : return ""
        
        ulSet = set(s)
        print(ulSet)
        
        for i,c in enumerate(s):
            if c.swapcase() not in ulSet:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                
                return s2 if len(s2) > len(s1) else s1
        return s
        

s = Solution()
print(s.longestNiceSubstring("Yazaay"))

print(set(
    'AAansAskaN'
))

print('a'.swapcase())