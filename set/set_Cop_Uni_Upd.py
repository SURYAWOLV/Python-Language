# Here are 20 advanced, real-time, interview-style Python questions covering `copy()`, `union()`, and `update()` methods with unique logic and data types.  

# ---

# ### **1. Copying a Set of Employee IDs**  
# **Question:**  
# A company maintains a set of employee IDs `{101, 102, 103, 104}`. Create a copy of this set. What will be the output of the copied set?  

# **Expected Output:**  
# `{101, 102, 103, 104}`  


from copy import copy, deepcopy
# shallowcopy
employee_id ={101,102,103,104}
copy_empolyee_id = copy(employee_id)
print(copy_empolyee_id)

# shallowcopy
ShallowCopy_empolyee_id = copy(employee_id)
print(ShallowCopy_empolyee_id)

# Deepcopy
DeepCopy_employee_id = deepcopy(employee_id)
print(DeepCopy_employee_id)

# ---

# ### **2. Copying a Set and Adding a New Element**  
# **Question:**  
# Given the set `{‘apple’, ‘banana’, ‘cherry’}`, create a copy and add `'mango'` to the copied set. What will be the original and copied set?  

# **Expected Output:**  
# Original: `{‘apple’, ‘banana’, ‘cherry’}`  
# Copied: `{‘apple’, ‘banana’, ‘cherry’, ‘mango’}`  

original={'apple','banana','cherry'}
copied = copy(original)
copied.add('mango')
print(f'orginal: {original}')
print(f'copied: {copied}')

# ---

# ### **3. Checking if Copying Creates a New Reference**  
# **Question:**  
# A set `{1, 2, 3}` is copied using `copy()`. If you modify the copied set by adding `4`, will the original set be affected?  

# **Expected Output:**  
# Original: `{1, 2, 3}`  
# Copied: `{1, 2, 3, 4}`  

original_1={1,2,3}
copied_1 = copy(original_1)
copied_1.add(4)
print(f'orginal: {original_1}')
print(f'copied: {copied_1}')

# ---

# ### **4. Using `copy()` on a Frozen Set**  
# **Question:**  
# If `frozenset({10, 20, 30})` is copied, will the new set be mutable or immutable?  

# **Expected Output:**  
# Immutable (since `frozenset` remains immutable after copying).  

# ---

# ### **5. Copying a Set Containing a Tuple**  
# **Question:**  
# A set `{(1, 2), (3, 4)}` is copied using `copy()`. If you add `(5,6)` to the copied set, what is the result?  

# **Expected Output:**  
# Original: `{(1, 2), (3, 4)}`  
# Copied: `{(1, 2), (3, 4), (5, 6)}`  

# ---

# ### **6. Copying a Set and Removing an Element**  
# **Question:**  
# A set `{‘A’, ‘B’, ‘C’}` is copied. If `'B'` is removed from the copied set, what will be the output?  

# **Expected Output:**  
# Original: `{‘A’, ‘B’, ‘C’}`  
# Copied: `{‘A’, ‘C’}`  

# ---

# ### **7. Union of Two Sets Containing Integers**  
# **Question:**  
# Given two sets `{1, 2, 3}` and `{3, 4, 5}`, find their union.  

# **Expected Output:**  
# `{1, 2, 3, 4, 5}`  

set_1 = {1,2,3}
set_2 ={3,4,5}
union_set3 = set_1.union(set_2)
print(union_set3)

# ---

# ### **8. Union of Two Sets Containing Strings**  
# **Question:**  
# Find the union of `{‘dog’, ‘cat’}` and `{‘parrot’, ‘fish’}`.  

# **Expected Output:**  
# `{‘dog’, ‘cat’, ‘parrot’, ‘fish’}`  

# ---

# ### **9. Union of a Set and an Empty Set**  
# **Question:**  
# What is the result of `{1, 2, 3} ∪ {}`?  

# **Expected Output:**  
# `{1, 2, 3}`  

# ---

# ### **10. Union of a Set and a Tuple Converted to a Set**  
# **Question:**  
# Compute `{1, 2, 3} ∪ set((4, 5, 6))`.  

# **Expected Output:**  
# `{1, 2, 3, 4, 5, 6}`  

union_set4 = set_1 | set_2
print(union_set4)

# ---

# ### **11. Union of a Set and a Frozen Set**  
# **Question:**  
# Find `{10, 20, 30} ∪ frozenset({40, 50})`.  

# **Expected Output:**  
# `{10, 20, 30, 40, 50}`  

# ---

# ### **12. Union of Sets with Overlapping Elements**  
# **Question:**  
# Find `{‘x’, ‘y’} ∪ {‘y’, ‘z’}`.  

# **Expected Output:**  
# `{‘x’, ‘y’, ‘z’}`  

# ---

# ### **13. Using `update()` to Add Elements from Another Set**  
# **Question:**  
# Update `{‘red’, ‘blue’}` with `{‘green’, ‘yellow’}` using `update()`. What is the result?  

# **Expected Output:**  
# `{‘red’, ‘blue’, ‘green’, ‘yellow’}`  

colors ={'red','blue'}
sub_colors ={'green','yellow'}
colors.update(sub_colors)
print(colors)

# ---

# ### **14. Using `update()` with a List**  
# **Question:**  
# Update `{1, 2, 3}` with elements from the list `[4, 5]`. What is the result?  

# **Expected Output:**  
# `{1, 2, 3, 4, 5}`  

my_list1 = [4,5]
my_set1 ={1,2,3,4}
my_set1.update(my_list1)
print(my_set1)

# ---

# ### **15. Using `update()` with a String**  
# **Question:**  
# Update `{‘A’, ‘B’}` with the string `'CD'`. What will be the result?  

# **Expected Output:**  
# `{‘A’, ‘B’, ‘C’, ‘D’}` (since a string is iterable, characters are added separately).  
x= {'A','B'}
x.update("CD")
print(x)

# ---

# ### **16. Using `update()` with a Dictionary**  
# **Question:**  
# Update `{‘name’, ‘age’}` with keys from `{'gender': 'M', 'city': 'NY'}`. What is the result?  

# **Expected Output:**  
# `{‘name’, ‘age’, ‘gender’, ‘city’}` (since `update()` adds dictionary keys, not values).  

# ---

# ### **17. Using `update()` with a Set Containing Different Data Types**  
# **Question:**  
# Update `{1, 'A'}` with `{2.5, (3, 4)}`. What is the result?  

# **Expected Output:**  
# `{1, 'A', 2.5, (3, 4)}`  

# ---

# ### **18. Using `update()` on an Empty Set**  
# **Question:**  
# An empty set `{}` is updated with `{‘hello’, ‘world’}`. What will be the result?  

# **Expected Output:**  
# `{‘hello’, ‘world’}`  

# ---

# ### **19. Using `update()` with a Frozen Set**  
# **Question:**  
# Update `{1, 2, 3}` with `frozenset({4, 5, 6})`. What is the result?  

# **Expected Output:**  
# `{1, 2, 3, 4, 5, 6}`  

# ---

# ### **20. Combining `copy()`, `union()`, and `update()`**  
# **Question:**  
# Given:  
# ```python
# A = {10, 20, 30}  
# B = {40, 50}  
# C = A.copy()  
# C.update(B)  
# D = C.union({60, 70})  
# ```
# What is `D`?  

# **Expected Output:**  
# `{10, 20, 30, 40, 50, 60, 70}`  

A = {10,20,30}
A.update({40,50})
c=deepcopy(A)
D = c | {60,70}
print(D)

# ---

# These questions provide a diverse range of scenarios for `copy()`, `union()`, and `update()`, ensuring no repetition in logic or data types.  🚀