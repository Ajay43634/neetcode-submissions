class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # no n-1 check, start counting from every number
            length = 1
            while n + length in numSet:
                length += 1
            longest = max(longest, length)
        
        return longest