class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l1 = []
        for i in nums:
            if i not in l1:
                l1.append(i)
            else:
                return i

