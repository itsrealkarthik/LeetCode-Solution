class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=""
        for item in zip(*strs):
            if(len(set(item))==1):
                string+=item[0]
            else:
                break
        return string