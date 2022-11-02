import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        str1 = str1.lower()
        ##print(str1)
        str2 = str1[::-1]
        return str1==str2