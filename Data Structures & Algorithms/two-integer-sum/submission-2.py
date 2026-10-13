class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        print(target)
        d = dict()
        for i, n in enumerate(nums):
            d[target - n] = i
        print(d)

        for i in range(len(nums)):
            if nums[i] in d and i != d[nums[i]] :
                return [i, d[nums[i]]]