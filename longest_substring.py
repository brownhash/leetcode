"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collection = []
        temp = []
        result = ""
        for char in s:
            if char not in temp:
                temp.append(char)
            else:
                if len(temp) > len(collection):
                    collection = temp
                temp = temp[temp.index(char)+1:]
                temp.append(char)
        if len(temp) > 0 and len(temp) > len(collection):
            collection = temp
        return len(result.join(collection))
