text= "hello Python"
new_text = text.replace("Python","World")
print(new_text)

rand_txt = "one two one two one"
count_occurrence = rand_txt.replace("one", "1", 2)
print(count_occurrence)

data = {"name": "John Doe", "city": "New York"}
new_data = {k: v.replace("o", "0") for k, v in data.items()}
print(new_data)  # Output: {'name': 'J0hn D0e', 'city': 'New Y0rk'}

text = "I am happy and excited"
new_text = text.replace("happy", "😊").replace("excited", "🎉")
print(new_text)  # Output: I am 😊 and 🎉
