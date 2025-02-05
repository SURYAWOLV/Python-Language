# Topic isdecimal

class IsDecimal:
    def practice_1(self,s):
        return s.isdecimal()

s = "12345"
lst = ["123", "45", "3.14", "²", "67"]
mixed_list = ["42", "hello", "100", "3.14", "98", "²"]
tup = ("789", "56a", "003", "½", "xyz")
my_dict = {"123": "valid", "abc": "invalid", "987": "valid", "²": "invalid"}
data = {"id1": "00123", "id2": "abc", "id3": "400", "id4": "³"}
my_set = {"456", "12x", "78", "hello", "³"}
nested_list = [["123", "abc"], ["456", "78x"], ["99", "⅓"]]
my_dict = {"one": "123", "two": "hello", "three": "456", "four": "xyz", "five": "²"}

obj = IsDecimal()
print(obj.practice_1(s))
