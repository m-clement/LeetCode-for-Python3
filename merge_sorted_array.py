class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1

        # Pointer for nums1 to insert the next maximum value
        p = m + n - 1

        # While there are still elements to consider in nums2
        while p2 >= 0:
            # If nums1 has no more elements or the current element of nums2 is greater than the current element of nums1
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1