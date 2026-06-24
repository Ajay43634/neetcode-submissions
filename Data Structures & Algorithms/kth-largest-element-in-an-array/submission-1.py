class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l1 = []
        for i in nums:
            l1.append(i)

            l1.sort(reverse=True)

            if(len(l1)>k):
                l1.pop()
        return(l1[-1])
        