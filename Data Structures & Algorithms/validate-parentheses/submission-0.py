class Solution:
    def isValid(self, s: str) -> bool:
        m={')':'(',']':'[','}':'{'}
        st=[]
        for c in s:
            if c in m:
                if not st or st.pop()!=m[c]:
                    return False
            else: st.append(c)
        return not st