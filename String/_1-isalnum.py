# Topic: isalnum()

class IsAlNum:
    def practiceTest_1(self, string):
        string.isalnum()
        return True
    def practiceTest_2(self, lis):
        count=0
        items =[]
        for item in lis:
            if item.isalnum():
                count +=1 
                items.append(item)
        return  f"Total Number items is isalnum: {count} and list {items}"
    # 3.Tuple (Check Individual String Elements)
    def practiceTest_3(self, tup):
        result = []
        for item in tup:
            result.append(item.isalnum())
        res=tuple(result)
        return res
    # 4. Set (Unique Alphanumeric Check)
    def practiceTest_4(self, set_s):
        result=set()
        for item in set_s:
            result.add(item.isalnum())
        return result
    # 5. Dictionary (Key and Value Check)
    def practiceTest_5(self, dict_s):
        result ={}
        for k,v in dict_s.items():
            result[k]=v.isalnum()
        return result
    # 6. List (Nested List of Strings)
    def practiceTest_6(self, Nestlis):
        result=[]
        for items in Nestlis:
            res=[]
            result.append(res)
            for item in items:
                if item.isalnum():
                    res.append(True)
                else:
                    res.append(False)
        return result
    # 7. Tuple (With Mixed Data Types)
    def practiceTest_7(self, tup):
        result=tuple([str(item).isalnum() for item in tup ])
        return result
    

    


        
    

    
obj=IsAlNum()
print(obj.practiceTest_1("Hello123"))
print(obj.practiceTest_2(["Hello123", "abc", "12345", "hello world"]))
print(obj.practiceTest_3(("apple123", "orange!", "456xyz")))
print(obj.practiceTest_4({"dog123", "cat!", "12345", "bird&"}))
print(obj.practiceTest_5({"username": "user123", "password": "pass!@#", "id": "456abc"}))
print(obj.practiceTest_6([["apple12", "hello123"], ["abc!", "world45"], ["xyz123", "456abc"]]))
print(obj.practiceTest_7(("text123", 456, 789.1)))
