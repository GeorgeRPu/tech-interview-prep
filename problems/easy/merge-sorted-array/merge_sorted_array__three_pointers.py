r"""
>>> from merge_sorted_array__three_pointers import merge
>>> nums1 = [1, 2, 3, 0, 0, 0]
>>> nums2 = [2, 5, 6]
>>> merge(nums1, 3, nums2, 3)
>>> nums1
[1, 2, 2, 3, 5, 6]
>>> nums1 = [1]
>>> nums2 = []
>>> merge(nums1, 1, nums2, 0)
>>> nums1
[1]
>>> nums1 = [0]
>>> nums2 = [1]
>>> merge(nums1, 0, nums2, 1)
>>> nums1
[1]
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    """Merge the n-length array ``nums2`` into the (m + n)-length array
    ``nums1``.
    """
    # shift all the elements of nums1 to be flush with the end of the list
    for i in range(m + n - 1, n - 1, -1):
        nums1[i] = nums1[i - n]
    for i in range(n):
        nums1[i] = 0

    # merge the two lists
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i + n] < nums2[j]:
            nums1[i + j] = nums1[i + n]
            i += 1
        else:
            nums1[i + j] = nums2[j]
            j += 1

    while i < m:
        nums1[i + j] = nums1[i + n]
        i += 1

    while j < n:
        nums1[i + j] = nums2[j]
        j += 1
