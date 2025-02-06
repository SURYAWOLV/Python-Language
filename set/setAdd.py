# Here are 20 advanced, real-time, interview-style questions focusing on Python's `set.add()` method. Each scenario is unique and covers different use cases.

# ---

# ### **1. Adding a New Employee ID to a Set**  
# **Question:**  
# A company maintains a set of employee IDs. Add a new employee ID `1056` to the set `{1001, 1002, 1003, 1004, 1005}`. What will be the updated set?  

# **Expected Output:**  
# `{1001, 1002, 1003, 1004, 1005, 1056}`  

employee_id ={1001,1002,1003,1004,1005,1056}
employee_id.add(1006)
print(employee_id)

# # new_employee=employee_id.add(1007)  # output: None
# # print(new_employee)

# ---

# ### **2. Adding a New Character to a Set of Vowels**  
# **Question:**  
# A program tracks vowels used in a paragraph. Add the vowel `'y'` to the existing set `{‘a’, ‘e’, ‘i’, ‘o’, ‘u’}`. What will be the output?  

# **Expected Output:**  
# `{'a', 'e', 'i', 'o', 'u', 'y'}`  

vowels={'a','e','i','o','u'}
vowels.add('y')
print(vowels)

# ---

# ### **3. Adding an Integer to a Set of Floating-Point Numbers**  
# **Question:**  
# A dataset contains floating-point numbers `{1.2, 3.4, 5.6}`. Add an integer `4` to this set. What is the resulting set?  

# **Expected Output:**  
# `{1.2, 3.4, 4, 5.6}`  

dataset ={1.2,3.4,5.6}
dataset.add(4)
print(dataset)

# ---

# ### **4. Adding a Tuple to a Set of Tuples**  
# **Question:**  
# A system stores coordinates as a set of tuples `{(1, 2), (3, 4)}`. Add a new coordinate `(5, 6)`. What will be the new set?  

# **Expected Output:**  
# `{(1, 2), (3, 4), (5, 6)}`  

coordinates ={(1,2),(3,4)}
coordinates.add((5,6))
print(coordinates)

# ---

# ### **5. Adding an Existing Element to a Set**  
# **Question:**  
# Consider the set `{10, 20, 30}`. If you try to add `20` again, what will be the output?  

# **Expected Output:**  
# `{10, 20, 30}` (No change, as sets do not allow duplicates.)  

set_numbers={10,20,30}
set_numbers.add(20)
print(set_numbers)

# ---

# ### **6. Adding a Boolean Value to a Set**  
# **Question:**  
# A system stores boolean values `{True}`. Add `False` to it. What will be the resulting set?  

# **Expected Output:**  
# `{True, False}`  

# ---

# ### **7. Adding `None` to a Set of Integers**  
# **Question:**  
# Given the set `{1, 2, 3}`, add `None` to it. What is the output?  

# **Expected Output:**  
# `{1, 2, 3, None}`  

# ---

# ### **8. Adding a Complex Number to a Set**  
# **Question:**  
# A program tracks unique complex numbers `{1+2j, 3+4j}`. Add `5+6j` to this set. What will be the updated set?  

# **Expected Output:**  
# `{(1+2j), (3+4j), (5+6j)}`  

unique_complex_numbers ={1+2j,3+4j}
unique_complex_numbers.add(5+6j)
print(unique_complex_numbers)

# ---

# ### **9. Adding a Frozen Set to a Set**  
# **Question:**  
# A set `{frozenset({1, 2}), frozenset({3, 4})}` is given. Add `frozenset({5, 6})` to it. What is the result?  

# **Expected Output:**  
# `{frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}`  

# ---

# ### **10. Adding a Single Character to an Empty Set**  
# **Question:**  
# An empty set `{}` is given. Add the character `'z'`. What is the result?  

# **Expected Output:**  
# `{'z'}`  

# ---

# ### **11. Adding a Large Number to a Set**  
# **Question:**  
# A set `{1, 2, 3}` is given. Add `9999999999`. What is the output?  

# **Expected Output:**  
# `{1, 2, 3, 9999999999}`  

# ---

# ### **12. Adding a Negative Number to a Set**  
# **Question:**  
# A set `{0, 1, 2}` is given. Add `-5`. What will be the result?  

# **Expected Output:**  
# `{0, 1, 2, -5}`  

# ---

# ### **13. Adding a Hexadecimal Value to a Set**  
# **Question:**  
# A set `{0x1, 0x2, 0x3}` is given. Add `0x4`. What is the updated set?  

# **Expected Output:**  
# `{1, 2, 3, 4}` (Hex values convert to integers.)

set_hexdec={0x1,0x2,0x3}
set_hexdec.add(0o4)
print(set_hexdec)  

# ---

# ### **14. Adding an Octal Number to a Set**  
# **Question:**  
# A set `{0o1, 0o2, 0o3}` is given. Add `0o4`. What is the resulting set?  

# **Expected Output:**  
# `{1, 2, 3, 4}`  

set_octdec={0o1,0o2,0o3}
set_octdec.add(0o4)
print(set_octdec)

# ---

# ### **15. Adding a Binary Number to a Set**  
# **Question:**  
# A set `{0b1, 0b10, 0b11}` is given. Add `0b100`. What is the output?  

# **Expected Output:**  
# `{1, 2, 3, 4}`  

set_bin = {0b1, 0b10 , 0b11}
set_bin.add(0b100)
print(set_bin)

# ---

# ### **16. Adding a Unicode Character to a Set**  
# **Question:**  
# A set `{‘A’, ‘B’}` is given. Add the Unicode character `'\u20AC'` (Euro sign). What will be the updated set?  

# **Expected Output:**  
# `{'A', 'B', '€'}`  

unicode_set ={'A','B'}
unicode_set.add('\u20AC')
print(unicode_set)

# ---

# ### **17. Adding an Emoji to a Set**  
# **Question:**  
# A set `{‘🙂’, ‘🙃’}` is given. Add the emoji `'😂'`. What will be the output?  

# **Expected Output:**  
# `{'🙂', '🙃', '😂'}`  

# ---

# ### **18. Adding a Decimal Object to a Set**  
# **Question:**  
# A set `{Decimal('1.1'), Decimal('2.2')}` is given. Add `Decimal('3.3')`. What will be the updated set?  

# **Expected Output:**  
# `{Decimal('1.1'), Decimal('2.2'), Decimal('3.3')}`

from decimal import Decimal
dec_obj ={Decimal('1.1'),Decimal('2.2')}
dec_obj.add(Decimal('3.3'))
print(dec_obj)  

# ---

# ### **19. Adding a Datetime Object to a Set**  
# **Question:**  
# A set containing `{datetime(2024, 1, 1), datetime(2025, 1, 1)}` is given. Add `datetime(2026, 1, 1)`. What is the result?  

# **Expected Output:**  
# `{datetime(2024, 1, 1), datetime(2025, 1, 1), datetime(2026, 1, 1)}`  

from datetime import datetime 
set_DMY ={datetime(2024,1,1),datetime(2025,1,1)}
set_DMY.add(datetime(2026,1,1))
print(set_DMY)

# ---

# ### **20. Adding a UUID to a Set**  
# **Question:**  
# A set `{UUID('123e4567-e89b-12d3-a456-426614174000')}` is given. Add `UUID('987e6543-e21b-45d3-b678-123456789abc')`. What is the updated set?  

# **Expected Output:**  
# `{UUID('123e4567-e89b-12d3-a456-426614174000'), UUID('987e6543-e21b-45d3-b678-123456789abc')}`  

from uuid import UUID
UUID_set ={UUID('123e4567-e89b-12d3-a456-426614174000')}
UUID_set.add(UUID('987e6543-e21b-45d3-b678-123456789abc'))
print(UUID_set)

# ---

