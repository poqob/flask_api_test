import sys
import json
import requests as req



uri=sys.argv[1]

response=req.get(url=uri)

class Model:
    def __init__(self,name="null",surname="null"):
        self.name=name
        self.surname=surname
    def __str__(self) -> str:
        return f"name: {self.name}\nsurname: {self.surname}"    


my_list=[]

json_obj= json.loads(response.text)

for key in json_obj:
    my_list.append(Model(name=json_obj[key]["name"],surname=json_obj[key]["surname"])) 

for x in my_list:
    print(f"{x}\n")





