# Here are 10 advanced, real-time, interview-style questions focusing on Python's `intersection()` and `intersection_update()` methods. Each scenario is unique and covers different use cases.  

# ---

# ### **1. Finding Common Employees Between Two Departments**  
# **Question:**  
# A company has two departments:  
# - HR department employees: `{101, 102, 103, 104, 105}`  
# - IT department employees: `{103, 104, 106, 107}`  

# Find the common employees between HR and IT departments.  

# **Expected Output:**  
# `{103, 104}`  

# *(Uses `intersection()`) 

HR_department_employees = {101, 102, 103, 104, 105}
IT_department_employees = {103, 104, 106, 107}
common_employees = IT_department_employees & HR_department_employees
print(common_employees)

# ---

# ### **2. Finding Common Letters in Two Words**  
# **Question:**  
# Two words are given as sets:  
# - `"engineering"` → `{‘e’, ‘n’, ‘g’, ‘i’, ‘r’}`  
# - `"management"` → `{‘m’, ‘a’, ‘n’, ‘g’, ‘e’, ‘t’}`  

# Find the common letters between these words.  

# **Expected Output:**  
# `{'e', 'n', 'g'}`  

# *(Uses `intersection()`)  

engineering = {'e', 'n', 'g', 'i', 'r'}
management = {'m', 'a', 'n', 'g', 'e', 't'}
common_letter = engineering.intersection(management)
print(common_letter)

# ---

# ### **3. Finding Common Elements in Multiple Lists**  
# **Question:**  
# Three sets of students participated in different coding contests:  
# - `{‘Alice’, ‘Bob’, ‘Charlie’}` (Hackathon)  
# - `{‘Charlie’, ‘David’, ‘Alice’}` (AI Challenge)  
# - `{‘Alice’, ‘Charlie’, ‘Eve’}` (Web Dev Contest)  

# Find the students who participated in all three contests.  

# **Expected Output:**  
# `{'Alice', 'Charlie'}`  

# *(Uses `intersection()`)  

# ---

# ### **4. Updating an Inventory Set with Common Items**  
# **Question:**  
# A store maintains inventory for two branches:  
# - Branch A: `{‘laptop’, ‘mouse’, ‘keyboard’, ‘monitor’}`  
# - Branch B: `{‘tablet’, ‘laptop’, ‘mouse’, ‘headphones’}`  

# Update Branch A’s inventory to retain only the common items with Branch B.  

# **Expected Output:**  
# `{'laptop', 'mouse'}`  

# *(Uses `intersection_update()`)  

# ---

# ### **5. Finding Common Digits Between Two Numbers**  
# **Question:**  
# Given two numbers: `287654` and `345678`, represent their digits as sets and find the common ones.  

# **Expected Output:**  
# `{3, 4, 5, 6, 7, 8}`  

# *(Uses `intersection()`)  

# ---

# ### **6. Identifying Common Courses Among Students**  
# **Question:**  
# Two students enrolled in different courses:  
# - Student A: `{‘Math’, ‘Physics’, ‘CS’, ‘English’}`  
# - Student B: `{‘Biology’, ‘Math’, ‘English’, ‘CS’}`  

# Find the common courses they are taking.  

# **Expected Output:**  
# `{'Math', 'CS', 'English'}`  

# *(Uses `intersection()`)  

# ---

# ### **7. Finding Common Security Permissions**  
# **Question:**  
# A system grants access permissions as follows:  
# - Admin: `{‘read’, ‘write’, ‘execute’, ‘delete’}`  
# - Editor: `{‘read’, ‘write’, ‘execute’}`  
# - Viewer: `{‘read’}`  

# Find the common permissions between Admin and Editor.  

# **Expected Output:**  
# `{'read', 'write', 'execute'}`  

# *(Uses `intersection()`)  

# ---

# ### **8. Retaining Common Social Media Followers**  
# **Question:**  
# Two influencers have overlapping followers:  
# - Influencer A: `{‘user1’, ‘user2’, ‘user3’, ‘user4’}`  
# - Influencer B: `{‘user3’, ‘user4’, ‘user5’, ‘user6’}`  

# Update Influencer A's follower list to retain only common followers.  

# **Expected Output:**  
# `{'user3', 'user4'}`  

# *(Uses `intersection_update()`)  

Influencer_A= {'user1', 'user2', 'user3', 'user4'}  
Influencer_B= {'user3', 'user4', 'user5', 'user6'} 
Influencer_c= {'user8', 'user7', 'user5', 'user6'} 
Influencer_A.intersection_update(Influencer_B)
print(Influencer_A)
Influencer_B = Influencer_B & Influencer_c 
print(Influencer_B)
# ---

# ### **9. Finding Common Special Characters in Passwords**  
# **Question:**  
# Two passwords contain special characters:  
# - Password 1: `{‘@’, ‘#’, ‘!’, ‘$’, ‘%’}`  
# - Password 2: `{‘*’, ‘#’, ‘!’, ‘&’}`  

# Find the common special characters.  

# **Expected Output:**  
# `{'#', '!'}`  

# *(Uses `intersection()`)  

# ---

# ### **10. Retaining Common Colors in Two Palettes**  
# **Question:**  
# A designer uses two color palettes:  
# - Palette A: `{‘red’, ‘blue’, ‘green’, ‘black’}`  
# - Palette B: `{‘yellow’, ‘green’, ‘blue’, ‘purple’}`  

# Update Palette A to keep only common colors.  

# **Expected Output:**  
# `{'blue', 'green'}`  

# *(Uses `intersection_update()`)  

# ---

# Each question presents a unique real-world scenario where `intersection()` and `intersection_update()` are useful.  🚀