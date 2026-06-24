class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            num_set = []
            for i in result:
                num_set.append(i+[num])
            result = result + num_set
        return(result)