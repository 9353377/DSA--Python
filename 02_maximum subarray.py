class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    solution = Solution()

    # Test cases with input and expected output
    test_cases = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.maxSubArray(nums)
        print(f"Test Case {i}:")
        print(f"  Input:  nums = {nums}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print("-" * 30)