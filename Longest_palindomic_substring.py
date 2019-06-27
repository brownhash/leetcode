"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def rev(a):
            if(str(a)==str(a)[::-1]):
                return(True)
            else:
                return(False)
        substring=""
        c=0
        i=0
        while(i<len(s)):
            pattern=s[c:i+1]
            if(rev(pattern)==True and len(pattern)>len(substring)):
                substring=str(pattern)
            if(i==len(s)-1):
                i=0
                c+=1
            else:
                i+=1
            if(c==len(s)):
                break
        return(substring)
