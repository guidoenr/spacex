from random import random
from constants import *

import random as rm
import requests, json

    
class c_Task:
    def __init__(self, title, description, category, type, idLabels, idMembers):
        self.title = title 
        self.description = description
        self.category = category
        self.type = type 
        self.idLabels = idLabels
        self.idMembers = idMembers

    def create_card(self):
        URL = BASE_URL + '/cards'
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
        try:
            requests.request('POST', URL, params=query)
            self.status = f'[OK]: Created {self.type}: {self.title} \n'
        except requests.exceptions.RequestException as re:
            self.status = f'[FAILED]: {re} \n'
        

class Issue(c_Task):
    def __init__(self, title, description):
        super().__init__(title, description, 'none', 'issue', [ID_ISSUE_LABEL], [])

class Bug(c_Task):
    def __init__(self, description):
        super().__init__(self.generate_random_title(), description, 'none', 'bug', [ID_BUG_LABEL], [self.generate_random_member()])
        
    def generate_random_title(self):
        word = rm.choice(WORDS)
        num = random()
        return f'bug-{word}-{num}'

    def generate_random_member(self):
        url = BASE_URL + f'/boards/{ID_BOARD}/members'
        response = requests.request('GET', url, params=AUTH)
        data = json.loads(response.content)
        random_member = rm.choice(data)["id"]
        return random_member

class Task(c_Task):
    def __init__(self, title, category):
        super().__init__(title, 'none', category, "task", [self.get_label_by_category(category)], [])

    def get_label_by_category(self, category):
        name = f"ID_{category.upper()}_LABEL"
        return globals()[name]
   
# issue = Issue("Issue Title", "Issue description")
# issue.create_card()

# bug = Bug("Bug description")
# bug.create_card()

# task = Task("Task title", "Task category")
# task.create_card()

