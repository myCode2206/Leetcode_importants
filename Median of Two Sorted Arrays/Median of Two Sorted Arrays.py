class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer = nums1+nums2
        mer.sort()
        if len(mer)%2 != 0:
            return mer[len(mer)//2]
        else:
            return (mer[len(mer)//2]+ mer[len(mer)//2-1])/2