class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=int, reverse=True)
        return nums[k-1]


        