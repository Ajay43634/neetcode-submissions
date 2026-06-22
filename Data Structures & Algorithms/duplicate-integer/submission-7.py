class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        l1 = []
        for i in nums:
            if(i in l1):
                return(True)
            else:
                l1.append(i)
        return(False)


