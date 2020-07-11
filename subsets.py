"""
QUESTION:
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums = list(sorted(nums))
        self.helper(nums, 0, [], result)
        
        return result
    
    def helper(self, nums, start_index, subset, result):

        result.append(list(subset))        
        
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            
            self.helper(nums, i + 1, subset, result)
            
            subset.pop()
        
