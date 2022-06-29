# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
     
        l,h=0,n-1
        while l<=h:
            m=(l+h)//2            
            if not isBadVersion(m):
                l=m+1                
            else:
                h=m-1
        return l
