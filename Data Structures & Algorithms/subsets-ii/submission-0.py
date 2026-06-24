class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]

        for num in nums:
            new_subset = []

            for i in result:
                new_subset.append(i+[num])
            result += new_subset


        set1 = set()
        for i in result:
            set1.add(tuple(i))
        

        f_result = []
        for i in set1:
            f_result.append(list(i))

        return(f_result)
        

        