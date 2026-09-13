# Note: Bubble Sort cant be used because it takes more time.
# Merge Sort algorithm is used to satify O(nlog(n)) time Complexity & Space complexity
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:  # If there is only one element in the array, return it
            return nums

        # Divide Logic
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)  # Input:nums = [5,2,3,1] --> left=[2,5] Sorted version
        right = self.sortArray(right)  # right=[1,3]

        # Conquere logic
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):  # If Odd length array is there on left
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):  # If Odd length array is there on right
            nums[k] = right[j]
            j += 1
            k += 1
        return nums