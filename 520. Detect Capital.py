class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        return (w.isupper() or w.islower() or w.istitle())