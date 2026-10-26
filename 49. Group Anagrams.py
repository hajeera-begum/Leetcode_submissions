'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Dictionary:
        # Key   -> tuple representing the frequency of 26 letters
        # Value -> list of words having that same frequency
        result = defaultdict(list)

        # Process each word one by one
        for word in strs:

            # Frequency array for letters a-z
            # Initially all counts are 0
            count = [0] * 26

            # Count each character in the current word
            for char in word:

                # Convert character to its index:
                # 'a' -> 0
                # 'b' -> 1
                # ...
                # 'z' -> 25
                index = ord(char) - ord("a")

                # Increase frequency of this character
                count[index] += 1

            # Lists cannot be dictionary keys,
            # so convert the frequency list into a tuple.
            key = tuple(count)

            # Add the word to its corresponding anagram group
            result[key].append(word)

        # Return only the grouped words.
        # result.values() returns a dict_values object,
        # so convert it into a list.
        return list(result.values())