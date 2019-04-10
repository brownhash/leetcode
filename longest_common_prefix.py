"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        if(strs):
            mini=len(strs[0])
            obj=strs[0]
            for i in strs:
                if(len(i)<mini):
                    mini=len(i)
                    obj=i
            
            for i in range(0,len(obj)):
                element=obj[i]
                count=0
                for j in strs:
                    if (element == j[i]):
                        count+=1
                    else:
                        return(ans)
                
                if(count==len(strs)):
                    ans+=obj[i]
        return(ans)
                    
