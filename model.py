task_d = {
    "type": {},
    "title": {},
    "description": {},
    "category": {}
}

class Issue:
    def __init__(self, title, desc):
        self.title = title 
        self.desc = desc 

class Bug:
    def __init__(self, desc):
        self.desc = desc 

class Task:
    def __init__(self, title, category):
        self.title = title
        self.category = category

_type = "issue"
print(_type.capitalize())
constructor = globals()[_type.capitalize()]
instance = constructor("title", "desc")

print(instance)