class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        m=False
        su=0
        for c in s:
            d[c]=1+d.get(c,0)
        print(d)
        for k,v in d.items():
            if v%2==0:
                su+=v
        
                print(k,v)
            else:
                m=True
                su+=v-1
                
        
        if m: return su+1
        
        return su
