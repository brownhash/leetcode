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
        if(s):
            result=[]
            def check(i):
                i = list(i)
                for x in i:
                    if(i.count(x) > 1):
                        return(False)
                return(True)

            for i in range(0,len(s)):
                temp = ""
                temp+=s[i]
                result.append(temp)
                for j in range(i,len(s)):
                    if(i!=j):
                        temp += s[j]
                        result.append(temp)
            max = 0
            for i in result:
                data = check(i)
                if(data == True):
                    length = len(i)
                    if(length > max):
                        max = length
            return(max)
        else:
            return(0)
