# Topic Upper, Lower, capitalize, Title, casefold, swapcase

class ULCTCS:
    # 1. Basic String Manipulation using lower()
    def practice_1(self,text):
        new_text=text.lower()
        return new_text
    # 2. Convert List of Strings to Uppercase
    def practice_2(self, words):
        new_list=[]
        for elm in words:
            new_list.append(elm.upper())
        return new_list
    # 3. Apply capitalize() to Tuple Elements
    def practice_3(self,names):
        res=[]
        for elm in names:
            res.append(elm.capitalize())
        result=tuple(res)
        return result
    # 4. Dictionary Keys to Title Case
    def practice_4(self,data):
        new_data={}
        for k,v in data.items():
            new_data[k.title()]=v
        return new_data
    # 5. Swap Case of Values in a Dictionary
    def practice_5(self,info):
        new_info ={}
        for k,v in info.items():
            new_info[k]=v.swapcase()
        return new_info
    # 6. Convert Set Elements to Casefolded Strings
    def practice_6(self,my_set):
        new_set =set()
        for elm in my_set:
            new_set.add(elm.casefold())
        return new_set
    # 7. Title Case Each Sentence in a Paragraph
    def practice_7(self, paragraph):
        sentences=paragraph.split(". ")
        res=[]
        for elm in sentences:
            res.append(elm.title())
        new_paragraph=". ".join(res)
        return new_paragraph
    # 8. Apply lower() to String Elements in a Mixed List
    def practice_8(self,mix_list):
        new_Misxed_list =[]
        for elm in mix_list:
            if isinstance(elm,str):
                new_Misxed_list.append(elm.lower())
            else:
                new_Misxed_list.append(elm)
        return new_Misxed_list
    # 9. Swap Case in a Nested Dictionary
    def practice_9(self,nest_dict):
        new_dict ={}
        for k,v in nest_dict.items():
            sub_dict ={}
            for sub_k, sub_v in v.items():
                sub_dict[sub_k]= sub_v.swapcase()
            new_dict[k]=sub_dict
        return new_dict
    # 10. Convert Tuple Elements to Casefold
    def practice_10(self,my_tup):
        return tuple(elm.casefold() for elm in my_tup)
    # 11. Title Case Sentences Stored in a List
    def practice_11(self,sen):
        return [elm.title() for elm in sen]
    # 12. Swap Case of All Strings in a List
    def practice_12(self,data):
        return [elm.swapcase() for elm in data]
    # 13. Apply upper() to Dictionary Values
    def practice_13(self,user_info):
        return {k:v.upper() for k,v in user_info.items()}
    # 14. Convert Numbers to Strings and Apply capitalize()
    def practice_14(self,num):
        new_lis=[]
        for i in num:
            new_lis.append(str(i).capitalize())
        return new_lis
    # 15. Title Case Elements in a Set
    def practice_15(self, myset):
        new_set=set()
        for elm in myset:
            new_set.add(elm.title())
        return new_set
    # 16. Convert List of Booleans to Strings and Apply swapcase()
    def prictice_16(self,boo):
        return [str(elm).swapcase() for elm in boo]
    # 17. Apply casefold() to Nested List Elements
    def practice_17(self,nest_list):
        new_list=[]
        for elm in nest_list:
            new_lis=[]
            for elm in elm:
                new_lis.append(elm.casefold())
            new_list.append(new_lis)
        return new_list
    # 20. Casefold All Values in a Mixed Dictionary
    def practice_18(self,mydict):
        return {k: (v.casefold() if isinstance(v,str) else v) for k,v in mydict.items()}
    
    
            
obj=ULCTCS()
text = "Hello World!" 
words = ["apple", "banana", "cherry"]
names = ("john", "peter", "alice")
data = {"first_name": "john", "last_name": "doe", "city": "new york"}
info = {"name": "John Doe", "role": "Software Engineer"}
my_set = {"PYTHON", "DJANGO", "FLASK"}
paragraph = "hello world. python is great. let's learn."
mixed_list = ["HELLO", 42, "WORLD", True, "PYTHON"]
nested_dict = {"user": {"name": "Alice", "country": "USA"}}
my_tuple = ("DJANGO", "FLASK", "FASTAPI")
sentences = ["hello world", "python programming", "code every day"]
data1 = ["HELLO", "world", "Python", "PROGRAMMING"]
user_info = {"name": "alice", "city": "london"}
numbers = [1, 2, 3, 4]
fruit_set = {"apple", "banana", "grape"}
nested_list = [["HELLO", "WORLD"], ["PYTHON", "DJANGO"]]
data_dict = {"name": "ALICE", "age": 25, "city": "NEW YORK"}
boolean_list=[True,False,True,True,False]

print(obj.practice_1(text))
print(obj.practice_2(words))
print(obj.practice_3(names))
print(obj.practice_4(data))
print(obj.practice_5(info))
print(obj.practice_6(my_set))
print(obj.practice_7(paragraph))
print(obj.practice_8(mixed_list))
print(obj.practice_9(nested_dict))
print(obj.practice_10(my_tuple))
print(obj.practice_11(sentences))
print(obj.practice_12(data1))
print(obj.practice_13(user_info))
print(obj.practice_14(numbers))
print(obj.practice_15(fruit_set))
print(obj.prictice_16(boolean_list))
print(obj.practice_17(nested_list))
print(obj.practice_18(data_dict))



       