from random import random
import random as rm
import requests, json

API_KEY = '77130712b79444a97ed470100c610371'
TOKEN = '31ffac51c1ecb8cd92f3d193ac7aed7b9deb5a6fc78e1794f440c24a563bd185'
words = ['rands', 'w0rd', 'inheritance',
                'another', 'simple', 'spacex',
                'etc']

ID_TODO_LIST = '61d8a79933e62e20d78c4555'
ID_DOING = '61d8a79933e62e20d78c4556'
ID_DONE = '61d8a79933e62e20d78c4557'       

class c_Task:
    def create_card(self):
        URL = 'https://api.trello.com/1/cards'
        query = {
            'key': API_KEY,
            'token': TOKEN,
            'idList': ID_TODO_LIST,
            'name': self.title, 
            'pos': 'bottom',
            'desc': self.description
        }
        response = requests.request('POST', URL, params=query)

class Issue(c_Task):
    def __init__(self, title, description, type):
        self.description = description
        self.type = type
        self.title = title


class Bug(c_Task):
    def __init__(self, description, type):
        self.description = description
        self.type = type
        self.title = self.generate_random_title()

    def generate_random_title(self):
        word = rm.choice(words)
        num = random()
        return f'bug-{word}-{num}'

 
class Task(c_Task):
    def __init__(self, title, category, type):
        self.type = type
        self.title = title 
        self.category = category 

# issue = Issue("Issue title", "Description", "issue")
# issue.create_card()

# bug = Bug("Bug description", "bug")
# bug.create_card()

task = Task("Task title", "Task category", "task")
task.create_card()