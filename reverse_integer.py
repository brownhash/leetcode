"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−2^31,  (2^31)−1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):

        if(x<0):
            if(x%10 == 0):
                n=x
                while(n%10==0):
                    n=n/10
                strn=-(int(str(abs(n))[::-1]))
            else:
                strn=-(int(str(abs(x))[::-1]))
            
        elif(x%10==0 and x>0):
            n=x
            while(n%10==0):
                n=n/10
            strn=int(str(n)[::-1])
            
        else:
            strn=int(str(x)[::-1])
            
        if(strn >(-2**31) and strn<((2**31)-1)):
            return(strn)
        else:
            return 0
