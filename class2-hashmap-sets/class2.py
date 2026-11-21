"""
HASH SETS & HASHMAPS
"""

# ==============================
# 1. HASH SETS
# ==============================

"""
- Stores unique values (no duplicates)
- Fast lookup: O(1) average
- Useful for checking if an element exists
- Does not support indexing
"""

# Create a set
seen = set()

# Add elements
seen.add(10)
seen.add(20)
seen.add(30)

# Check if element exists
if 20 in seen:
    print("Found!")

# Remove an element
seen.remove(20)

# Duplicates
seen = {1, 2, 3, 3, 3}
print(seen)  # {1, 2, 3}


# ==============================
# 2. HASHMAPS (DICTIONARIES)
# ==============================

"""
- Stores key-value pairs
- Keys must be unique
- Values can be duplicated
- Fast lookup: O(1) average
- Useful for counting, storing indices, and tracking information
"""

# Create a hashmap
hashmap = {}

# Add key-value pairs
hashmap["apple"] = 3
hashmap["banana"] = 5

# Access a value
print(hashmap["apple"])  # 3

# Check if KEY exists
if "apple" in hashmap:
    print("Found!")

# Update a value
hashmap["apple"] = 10

# Remove a key
del hashmap["banana"]


# ==============================
# 3. HASHMAP .get()
# ==============================

"""
hashmap.get(key, default)

- Returns the value if the key exists
- Otherwise returns the default value
- Commonly used for counting frequencies
"""

counts = {}

nums = [1, 2, 2, 3, 3, 3]

for num in nums:
    counts[num] = counts.get(num, 0) + 1

print(counts)  # {1: 1, 2: 2, 3: 3}


# ==============================
# 4. SET VS HASHMAP
# ==============================

"""
SET:
- Stores values
- Checks if something exists
- Example: {1, 2, 3}

HASHMAP:
- Stores key-value pairs
- Associates information with a key
- Example: {1: 2, 2: 3, 3: 1}

When to use:

Set -> Have I seen this number before?
Hashmap -> How many times have I seen this number?
Hashmap -> At what index did I see this number?
"""


# ==============================
# 5. TIME & SPACE COMPLEXITY
# ==============================

"""
Operation               Set          Hashmap
------------------------------------------------
Insert                  O(1)         O(1)
Search                  O(1)         O(1)
Delete                  O(1)         O(1)

* Average-case time complexity

Space Complexity:
- O(n) if storing n unique elements or key-value pairs

Trade-off:
- We use additional memory to make lookups faster
"""


# ==============================
# 6. LEETCODE PATTERNS
# ==============================

"""
Pattern 1: Checking duplicates
-> Use a SET

Pattern 2: Counting frequencies
-> Use a HASHMAP

Pattern 3: Finding indices
-> Use a HASHMAP

"""

# ==============================
# 7. LEETCODE PROBLEMS
# ==============================

'''
"""
========================================
1. LEETCODE 217 - CONTAINS DUPLICATE
Topic: Hash Set
Difficulty: Easy
========================================

Given an integer array nums, return True if
any value appears at least twice.
Otherwise, return False.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4]
Output: True

Time Complexity:
Space Complexity:
"""

def containsDuplicate(nums):
    pass


"""
========================================
2. LEETCODE 1 - TWO SUM
Topic: Hashmap
Difficulty: Easy
========================================

Given an integer array nums and an integer
target, return the indices of two numbers
that add up to target.

You cannot use the same element twice.
Exactly one valid solution exists.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Time Complexity:
Space Complexity:
"""

def twoSum(nums, target):
    pass


"""
========================================
3. LEETCODE 242 - VALID ANAGRAM
Topic: Hashmap / Frequency Counting
Difficulty: Easy
========================================

Given two strings s and t, return True if
t is an anagram of s. Otherwise, return False.

Anagram:
Two strings containing the same characters
with the same frequencies, but possibly
in a different order.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Example 3:
Input: s = "aacc", t = "ccac"
Output: False

Time Complexity:
Space Complexity:
"""

def isAnagram(s, t):
    pass


# ========================================
# TEST CASES
# ========================================

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

'''