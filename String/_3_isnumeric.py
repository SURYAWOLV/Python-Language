# Topic isnumeric()

class IsNumeric:
    def practice_1(self, text):
        result = text.isnumeric()
        return result
    def practice_2(self,items):
        result =[]
        for elm in items:
            result.append(elm.isnumeric())
        return result
    def practice_3(self, data):
        result=tuple([True if elm.isnumeric() else False for elm in data])
        return result
    def pratice_4(self,numbers):
        result=set(True if elm.isnumeric() else False for elm in numbers)
        return result
    def practice_5(self,info):
        result= {info[k]:v.isnumeric()  for k,v in info.items()}
        return result
    def practice_6(self,nested_list):
        result=[[elm.isnumeric() for elm in item]for item in nested_list]
        return result
    def practice_7(self,mixed_set):
        result=set()
        for elm in mixed_set:
            if isinstance(elm, str):
                result.add(elm.isnumeric())
            else:
                result.add(False)
        return result

text = "123456"
items = ["123", "456", "789", "abc123"]
data = ("123", "456", "78abc", "23456")
numbers = {"123", "456", "789", "abc"}
info = {"key1": "123", "key2": "abc", "key3": "4567"}
nested_list = [["123", "456"], ["abc", "789"], ["1111", "2345"]]
datas = ("123", 456, 789.1)
mixed_set = {123, "456", "789abc", "1000"}
info = {1: "1234", "key2": "5678", 3.5: "9876"}
mixed_list = ["1234", 5678, 90.1, "abcd"]

obj = IsNumeric()
print(obj.practice_1(text))
print(obj.practice_2(items))
print(obj.practice_3(data))
print(obj.pratice_4(numbers))
print(obj.practice_5(info))
print(obj.practice_6(nested_list))
print(obj.practice_7(mixed_set))
