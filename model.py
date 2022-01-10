from random import random
import random as rm
import requests, json
from credentials import credentials as cre

words = ['rands', 'w0rd', 'inheritance',
                'another', 'simple', 'spacex',
                'etc']

ID_TODO_LIST = cre['id_todo_list']
ID_BOARD = cre['id_board']
TOKEN = cre['token']
API_KEY = cre['api_key']

class c_Task:
    def __init__(self, title, description, category, type, idLabels, idMembers):
        self.title = title 
        self.description = description
        self.category = category
        self.type = type 
        self.idLabels = idLabels
        self.idMembers = idMembers

    def create_card(self):
        URL = 'https://api.trello.com/1/cards'
        query = {
            'key': API_KEY,
            'token': TOKEN,
            'idList': ID_TODO_LIST,
            'name': self.title, 
            'pos': 'bottom',
            'desc': self.description,
            "idLabels": self.idLabels,
            "idMembers": self.idMembers
        }
        response = requests.request('POST', URL, params=query)

class Issue(c_Task):
    def __init__(self, title, description):
        super().__init__(title, description, 'none', 'issue', [], [])

class Bug(c_Task):
    def __init__(self, description):
        super().__init__(self.generate_random_title(), description, 'none', 'bug', [], [self.generate_random_member()])
        
    def generate_random_title(self):
        word = rm.choice(words)
        num = random()
        return f'bug-{word}-{num}'

    def generate_random_member(self):
        url = 'https://api.trello.com/1/boards/{ID_BOARD}/members'
        response = requests.request('GET', url)
        print(response.data)

class Task(c_Task):
    def __init__(self, title, category):
        super().__init__(title, 'none', category, "task", [], [])
   


# issue = Issue("Issue Title", "Issue description")
# issue.create_card()

bug = Bug("Bug description")
bug.generate_random_member()

# task = Task("Task title", "Task category")
# task.create_card()