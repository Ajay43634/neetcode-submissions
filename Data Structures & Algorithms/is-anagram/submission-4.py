class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [i for i in s]
        l2 = [i for i in t]
        if(len(s) == len(t)):
            for i in l1:
                if(i in l2):
                    l2.remove(i)
            if(len(l2)==0):
                return(True)
            else:
                return(False)
        return(False)
            