class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zero_count = nums.count(0)

        prod = 1
        for num in nums:
            if num != 0:
                prod *= num

        for i in range(len(nums)):
            if zero_count == 1:
                res.append(prod if nums[i] == 0 else 0)
            elif zero_count > 1:
                res.append(0)
            else:
                res.append(prod//nums[i])

        
        return res