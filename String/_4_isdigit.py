# Topic isdigit()

class IsDigit:
    def practice_1(self,s):
        return s.isdigit()  # 1. Basic Usage with a String
    def practice_2(self,lst ):
        result=[]
        for elm in lst:
            result.append(elm.isdigit())    #2. Checking Each Element in a List
        return result
    def practice_3(self,mixed_list):   #3. Filtering Digits from a Mixed List
        res=[]
        for elm in mixed_list:
            if elm.isdigit:
                res.append(elm)
        return res
    def practice_4(self,tup): #4. Checking Digits in a Tuple
        res=tuple([elm.isdigit() for elm in tup])
        return res
    def practice_5(self,my_dict): #5. Checking Keys in a Dictionary
        res= {k: k.isdigit() for k in my_dict.keys()}
        return res
    def practice_6(self,data): #6. Checking Dictionary Values
        res={}
        for val in data:
            res[val]=val.isdigit()
        return res
    def practice_7(self,my_set): #7. Checking Each Element in a Set
        res={}
        for elm in my_set:
            res[elm] =elm.isdigit()
        return res
    def practice_8(self):  #8. Checking Input from User
        user_input= input("Enter a String:")
        if user_input.isdigit():
            return f"you entered a valid number string"
        else:
            return f"invalid input"
    def practice_9(self,nested_list): #9. Checking Digits in a Nested List
        res =[[item.isdigit() for item in elm]for elm in nested_list]
        return res
    def practice_10(self,my_dicti):            # 10. Extracting Only Digit Strings from a Mixed Dictionary
        res={}
        for k,v in my_dicti.items():
            if v.isdigit():
                res[k]=v
        return res

s = "12345"
lst = ["123", "45", "abc", "67"]
mixed_list = ["42", "hello", "100", "3.14", "98"]
tup = ("789", "56a", "003", "xyz")
my_dict = {"123": "valid", "abc": "invalid", "987": "valid"}
data = {"id1": "00123", "id2": "abc", "id3": "400"}
my_set = {"456", "12x", "78", "hello"}
nested_list = [["123", "abc"], ["456", "78x"], ["99", "0"]]
my_dicti = {"one": "123", "two": "hello", "three": "456", "four": "xyz"}

obj=IsDigit()

print(obj.practice_1(s))
print(obj.practice_2(lst))
print(obj.practice_3(mixed_list))
print(obj.practice_4(tup))
print(obj.practice_5(my_dict))
print(obj.practice_6(data))
print(obj.practice_7(my_set))
print(obj.practice_8())
print(obj.practice_9(nested_list))
print(obj.practice_10(my_dicti))
