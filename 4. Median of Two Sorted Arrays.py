"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 """
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        i=0
        j=0
        merge=[]
        while (i<m and j<n):
                if nums1[i]<nums2[j]:
                        merge.append(nums1[i])
                        i+=1
                else:
                        merge.append(nums2[j])
                        j+=1
        while(i<m):
                merge.append(nums1[i])
                i+=1
        while(j<n):
                merge.append(nums2[j])
                j+=1
        if len(merge)%2==1:
                return merge[len(merge//2)]
        else:
                return (merge[len(merge)//2]+merge[len(merge)//2 -1])/2.0
        
nums1 =[1,2]
nums2 =[3,4]
print(findMedianSortedArrays(nums1,nums2))