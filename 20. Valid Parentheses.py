class Solution:
    def isValid(self, s: str) -> bool:
        corresponding={
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack=[]
        s=list(s)
        for i in s:
            if i in corresponding.keys():
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else:
                    element=stack.pop()
                    if corresponding.get(element)!=i:
                        return False
        if(len(stack)==0):
            return True
        else: return False