from random import random
import random as rm

api_key = ''
words = ['rands', 'w0rd', 'inheritance',
                'another', 'simple', 'spacex',
                'etc']


class Issue:
    def __init__(self, title, description, type):
        self.description = description
        self.type = type
        self.title = title

class Bug:
    def __init__(self, description, type):
        self.description = description
        self.type = type
        self.title = self.generate_random_title()

    def generate_random_title(self):
        word = rm.choice(words)
        num = random()
        return f'bug-{word}-{num}'

        
class Task:
    def __init__(self, title, category, type):
        self.type = type
        self.title = title 
        self.category = category 