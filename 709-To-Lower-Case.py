class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in s:
            if i >='A' and i <='Z':
                ans+=chr(ord(i)+32)
            else:
                ans+=i
        return ans