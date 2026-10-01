'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        index = []
        k = len(p)
        target = sorted(p)  # target is a list
        for i in range(len(s) - k + 1):  # Eg: s='abc' p='bca' length would be 0.So +1
            string = s[i:i + k]
            if sorted(string) == target:  # target is a list, so we are doing sorted(string)
                index.append(i)
        return index

#Time Complexity: O(n × k log k)