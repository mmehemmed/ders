# 1. Two Sum
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# 9. Palindrome Number
def is_palindrome(x):
    return str(x) == str(x)[::-1]

# 13. Roman to Integer
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            total += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            total += roman[s[i]]
    return total

# 14. Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

# 20. Valid Parentheses
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# 21. Merge Two Sorted Lists
def merge_two_lists(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    return result + list1 + list2

# 26. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# 27. Remove Element
def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# 28. Find the Index of the First Occurrence in a String
def str_str(haystack, needle):
    return haystack.find(needle)

# 35. Search Insert Position
def search_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

# 58. Length of Last Word
def length_of_last_word(s):
    words = s.strip().split()
    return len(words[-1])

# 66. Plus One
def plus_one(digits):
    num = int(''.join(map(str, digits))) + 1
    return list(map(int, str(num)))

# 67. Add Binary
def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# 69. Sqrt(x)
def my_sqrt(x):
    i = 0
    while i * i <= x:
        i += 1
    return i - 1

# 70. Climbing Stairs
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
# 88. Merge Sorted Array
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

#100. Same Tree
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
