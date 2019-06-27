"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        flag=0
        ind=0
        ind2=0
        if(len(nums1)%2!=0):
            ind=len(nums1)//2
        else:
            flag=1
            ind=len(nums1)//2
            ind2=ind-1
        
        if(flag==0):
            result=nums1[ind]
            return(float(result))
        elif(flag==1):
            result=(nums1[ind]+nums1[ind2])/2
            return(float(result))
