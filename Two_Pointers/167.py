class Solution:

  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]

      if current_sum == target:
        return [left + 1, right + 1]
      elif current_sum < target:
        left += 1
      else:
        right -= 1


# --- Execution block for VS Code ---
if __name__ == "__main__":
  # Create an instance of the Solution class
  solver = Solution()

  # Test Case
  numbers = [2, 7, 11, 15]
  target = 9

  result = solver.twoSum(numbers, target)

  print(f"Input: numbers = {numbers}, target = {target}")
  print(f"Output: {result}")