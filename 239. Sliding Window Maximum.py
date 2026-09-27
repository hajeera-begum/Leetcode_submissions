'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:
Input: nums = [1], k = 1
Output: [1]
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)  # Array length
        result = []  # Empty list to store the result
        dq = deque()  # To perform adding & deleting

        l = r = 0  # Left & right pointers to slide the window

        while r < n:  # While right pointer is less than array length
            # Step 1: Remove all the small elements
            while dq and nums[r] >= nums[dq[
                -1]]:  # While dq is not empty and value of right pointer is >= last value of the deque. Note: Deque is maintained in a decreasing order
                dq.pop()  # Just Pop, we are storing anything anywhere.
            # Step 2: Add Current Index
            dq.append(r)  # Append this left most value to dq
            # Step 3: Remove out of bound Index
            if dq[0] < l:  # First index of dq is less than left pointer
                dq.popleft()  # Removing from left
            # Step 4: Add the result
            if r + 1 >= k:
                result.append(nums[dq[0]])
                l += 1
            r += 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(k)