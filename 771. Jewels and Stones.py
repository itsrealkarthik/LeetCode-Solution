class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> list:
        listJewels = list(jewels)
        return sum(item in listJewels for item in stones)