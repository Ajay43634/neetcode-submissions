class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for n, freq in count.items():
            if(freq>1):
                return(True)
        return(False)
        