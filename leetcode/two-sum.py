class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	m = {}
        for i, num in enumerate(nums):
            diff: int = target - num
            if diff in m:
                return [i, m[diff]]
            m[num] = i
        return [0, 0]
