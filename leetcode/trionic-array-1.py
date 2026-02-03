class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        # Go until you stop increasing
        prev: int = nums[0] - 1
        idx_0: int = 0
        for i, val in enumerate(nums):
            if val < prev:
                # we are starting to decrease
                break
            elif val == prev:
                # this is a problem
                return False
            else:
                idx_0 = i

            prev = val

        if idx_0 <= 0 or idx_0 >= len(nums) - 1:
            # this means that we didn't go far enough
            return False


        idx_1: int = idx_0
        # Go until you stop decreasing
        for i, val in enumerate(nums[idx_0:], start=idx_0):
            if val > prev:
                # we are starting to increase
                break
            elif val == prev and i != idx_0: 
                # we have an issue
                return False
            else:
                idx_1 = i

            prev = val

        if idx_1 <= idx_0 or idx_1 >= len(nums) - 1:
            return False
        
        for i in range(idx_1 + 1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False

        # We have found a match
        return True
