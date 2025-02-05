# Topic Join

# 1. Joining a List of Strings
words = ["Hello", "World", "Python"]
def practice_1(wo):
    res = " ".join(wo)
    return res
print(practice_1(words))

# 2. Joining(-) Characters of a String
string = "Python"

# 3. Joining a Tuple of Strings
words_tuple = ("Join", "method", "in", "Python")

# 4. Joining a Set of Strings
words_set = {"apple", "banana", "cherry"}

# 5. Joining Keys of a Dictionary
data = {"name": "Alice", "age": "25", "city": "New York"}
def practice_2(da):
    res = ", ".join(da.keys())
    return res
print(practice_2(data))

# 13. Joining with Unicode Characters
words = ["Python", "is", "awesome"]
result = "🔥".join(words)
print(result)  # Output: Python🔥is🔥awesome

# 14. Joining Bytes (After Decoding)
byte_data = [b'hello', b'world']
by_da=b'hello'
def practice_3(byt, byd):
    res= " ".join(i.decode() for i in byt)
    result="".join(byd.decode())
    return f"{res} and {result}"
print(practice_3(byte_data,by_da))

# 17. Joining List with a Conditional Check
words_1 = ["Python", "", "Django", "", "REST"]
new_words=[]
for elm in words_1:
    if elm:
        new_words.append(elm)
join_words =" ".join(new_words)
print(join_words)

# 18. Joining Encrypted Text (ASCII Shift)

password= "Python"
encrypted_pass =""
for elm in password:
    num=ord(elm)+1
    char=chr(num)
    encrypted_pass += char
print(encrypted_pass)
orginal_pass=""
for elm in encrypted_pass:
    num=ord(elm) - 1
    char=chr(num)
    orginal_pass += char
print(orginal_pass)
print(" ".join(encrypted_pass))

import json
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
parsed = json.loads(json_data)
result = ", ".join(parsed.keys())
print(result)  # Output: name, age, city






