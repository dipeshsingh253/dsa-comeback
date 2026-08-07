class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in visited:
                return [visited[rem], i]

            visited[nums[i]] = i

        return [0,0] 