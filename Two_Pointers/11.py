class Solution(object):

  def maxArea(self, height):
    """:type height: List[int]

    :rtype: int
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
      width = right - left
      current_water = width * min(height[left], height[right])
      max_water = max(max_water, current_water)

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return max_water


# --- Example Input and Execution ---
if __name__ == "__main__":
  sol = Solution()

  # Test input
  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

  # Run the function
  output = sol.maxArea(height)

  # Display input and output
  print(f"Input: height = {height}")
  print(f"Output: {output}")