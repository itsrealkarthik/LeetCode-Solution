class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.match("^"+p+"$",s):
            return True
        return False