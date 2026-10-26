#217


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    nums = [int(x) for x in user_input.split()]
    
    sol = Solution()
    result = sol.containsDuplicate(nums)
    print("Contains duplicate:", result)