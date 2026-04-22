class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # brute
        # define a counter for a loop (n = 2)
        # define a new array
        # loop over and append items for duration of loop counter

        concat_arr = []
        for i in range(2):
            for num in nums:
                concat_arr.append(num)
        
        return concat_arr