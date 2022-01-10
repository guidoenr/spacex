from random import random
import random as rm
import requests, json
from credentials import credentials as cre

words = ['rands', 'w0rd', 'inheritance',
                'another', 'simple', 'spacex',
                'etc']

class c_Task:
    def __init__(self, title, description, category, type):
        self.title = title 
        self.description = description
        self.category = category
        self.type = type 

    def create_card(self):
        URL = 'https://api.trello.com/1/cards'
        query = {
            'key': cre['api_key'],
            'token': cre['token'],
            'idList': cre['id_todo_list'],
            'name': self.title, 
            'pos': 'bottom',
            'desc': self.description
        }
        response = requests.request('POST', URL, params=query)

class Issue(c_Task):
    def __init__(self, title, description):
        super().__init__(title, description, 'none', 'issue')

class Bug(c_Task):
    def __init__(self, description):
        super().__init__(self.generate_random_title(), description, 'none', 'bug')
        
    def generate_random_title(self):
        word = rm.choice(words)
        num = random()
        return f'bug-{word}-{num}'

 
class Task(c_Task):
    def __init__(self, title, category):
        super().__init__(title, 'none', category, "task")
   


# issue = Issue("Issue Title", "Issue description")
# issue.create_card()

# bug = Bug("Bug description")
# bug.create_card()

task = Task("Task title", "Task category")
task.create_card()