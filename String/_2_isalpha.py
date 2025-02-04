# Topic: isalpha()

class IsAlpha:
    def practice_1(self, text):
        result = text.isalpha()
        return result
    def practice_2(self,items):
        result =[]
        for item in items:
            result.append(item.isalpha())
        return result
    def practice_3(self, data):
        res=[]
        for elm in data:
            res.append(elm.isalpha())
        return tuple(res)
    def practice_4(self, unique_words):
        result =set()
        for elm in unique_words:
            result.add(elm.isalpha())
        return result
    def practice_5(self,user_info):
        result={}
        for k,v in user_info.items():
            result[k] = v.isalpha()
        return result
    def practice_6(self,nested_list):
        result =[]
        for items in nested_list:
            res =[]
            result.append(res)
            for elm in items:
                res.append(elm.isalpha())
        return result
    def practice_7(self,datas):
        result = tuple([str(elm).isalpha() for elm in datas])
        return result
    def practice_8(self, mixed_set):
        result = set([str(elm).isalpha() for elm in mixed_set])
        return result
    def practice_9(self, info):
        result ={k : v.isalpha() for k,v in info.items()}
        return result
text = "Hello"
items = ["apple", "banana", "123", "hello world"]
data = ("apple", "orange", "hello123", "grape")
unique_words = {"dog", "cat", "fish123", "bird"}
user_info = {"username": "johnDoe", "password": "pass123", "location": "newYork"}
nested_list = [["apple", "banana"], ["grape", "123"], ["orange", "pineapple"]]
datas = ("apple", 456, "hello", 78.9)
mixed_set = {123, "apple", "hello world", "orange"}
info = {"name": "John", "age": "25", "city": "Paris"}
mixed_list = ["hello", 123, "world", 45.67]  
obj = IsAlpha()
print(obj.practice_1(text))
print(obj.practice_2(items))
print(obj.practice_3(data))
print(obj.practice_4(unique_words))
print(obj.practice_5(user_info))
print(obj.practice_6(nested_list))
print(obj.practice_7(datas))
print(obj.practice_8(mixed_set))
print(obj.practice_9(info))
            

        

