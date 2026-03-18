"""
Problem
-------
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array ``nums`` sorted in **non-decreasing order**,
remove some duplicates
`in-place <https://en.wikipedia.org/wiki/In-place_algorithm>`__ such
that each unique element appears **at most twice**. The **relative
order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some
languages, you must instead have the result be placed in the **first
part** of the array ``nums``. More formally, if there are ``k`` elements
after removing the duplicates, then the first ``k`` elements of
``nums`` should hold the final result. It does not matter what you leave
beyond the first ``k`` elements.

Return ``k`` *after placing the final result in the first* ``k`` *slots
of* ``nums``.

Do **not** allocate extra space for another array. You must do this by
**modifying the input array**
`in-place <https://en.wikipedia.org/wiki/In-place_algorithm>`__ with
O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

::


   int[] nums = [...]; // Input array
   int[] expectedNums = [...]; // The expected answer with correct length

   int k = removeDuplicates(nums); // Calls your implementation

   assert k == expectedNums.length;
   for (int i = 0; i < k; i++) {
       assert nums[i] == expectedNums[i];
   }

If all assertions pass, then your solution will be **accepted**.

 

**Example 1:**

::


   Input: nums = [1,1,1,2,2,3]
   Output: 5, nums = [1,1,2,2,3,_]
   Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
   It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

::


   Input: nums = [0,0,1,1,1,1,2,3,3]
   Output: 7, nums = [0,0,1,1,2,3,3,_,_]
   Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
   It does not matter what you leave beyond the returned k (hence they are underscores).

 

**Constraints:**

- ``1 <= nums.length <= 3 * 10``\ :sup:```4```
- ``-10``\ :sup:```4```\ ``<= nums[i] <= 10``\ :sup:```4```
- ``nums`` is sorted in **non-decreasing** order.

Solution
--------
Position ``i = 2`` to start from the third element of ``nums``. If the current
element ``nums[i]`` equals the element two indices before ``nums[i - 2]``, look
ahead to the next element by incrementing an offset. If the current element
``nums[i + offset]`` is unequal to ``nums[i - 2]``, then copy
``nums[i + offset]`` to ``nums[i]`` and increment ``i``. Repeat until
``i + offset`` is out of bounds.

Code
----

.. literalinclude:: ../solutions/medium/RemoveDuplicatesFromSortedArrayII.py
    :language: python
    :lines: 105-

Test
----
>>> from RemoveDuplicatesFromSortedArrayII import removeDuplicates
>>> nums = [1, 1, 1, 2, 2, 3]
>>> k = removeDuplicates(nums)
>>> nums[:k]
[1, 1, 2, 2, 3]
>>> nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
>>> k = removeDuplicates(nums)
>>> nums[:k]
[0, 0, 1, 1, 2, 3, 3]
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """Removes duplicates from the sorted array ``nums`` in-place such that
    each element appears at most twice.
    """
    offset = 0
    i = 2
    while i + offset < len(nums):
        if nums[i + offset] == nums[i - 2]:
            offset += 1
        else:
            nums[i] = nums[i + offset]
            i += 1

    return len(nums) - offset
