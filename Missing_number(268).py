# 268

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    nums = [int(x) for x in user_input.split()]
    
    sol = Solution()
    result = sol.missingNumber(nums)
    print("Missing number:", result)