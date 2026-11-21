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

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False

Approach:
1. Create an empty set.
2. Loop through each number.
3. Check if number exists in set.
4. If it exists, return True.
5. Otherwise, add number to set.
6. Return False if no duplicates.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


"""
========================================
2. LEETCODE 1 - TWO SUM
Topic: Hashmap
Difficulty: Easy
========================================

Given an array nums and an integer target,
return the indices of two numbers that add
up to target.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Approach:
1. Create an empty hashmap.
2. Loop through each index.
3. Calculate complement = target - nums[i].
4. Check if complement exists in hashmap.
5. If found, return both indices.
6. Otherwise, store number and index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return [seen[diff], i]

        seen[nums[i]] = i


"""
========================================
3. LEETCODE 242 - VALID ANAGRAM
Topic: Hashmap / Frequency Counting
Difficulty: Easy
========================================

Given two strings s and t, return True if
t is an anagram of s.

Anagram = same characters, same frequencies,
but potentially different order.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Approach:
1. Check if string lengths are equal.
2. Create two empty hashmaps.
3. Count characters in the first string.
4. Count characters in the second string.
5. Compare both hashmaps.
6. Return True if they match.

Time Complexity: O(n)
Space Complexity: O(1) - fixed 26 lowercase letters
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t


# ========================================
# TEST CASES
# ========================================

print(containsDuplicate([1, 2, 3, 1]))       # True
print(containsDuplicate([1, 2, 3, 4]))       # False

print(twoSum([2, 7, 11, 15], 9))              # [0, 1]
print(twoSum([3, 2, 4], 6))                   # [1, 2]

print(isAnagram("anagram", "nagaram"))        # True
print(isAnagram("rat", "car"))                # False


'''