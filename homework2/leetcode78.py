from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q=[[]]
        n=len(nums)
        for i in range(n):
            for j in range(len(q)):
                q.append(q[j]+[nums[i]])
        return q