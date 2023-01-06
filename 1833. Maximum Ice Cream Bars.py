class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in accumulate(costs):
            if i<=coins:
                count+=1
            else:
                return count
        return count  