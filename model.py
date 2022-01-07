from random import random
import random as rm

api_key = '77130712b79444a97ed470100c610371'
token = '31ffac51c1ecb8cd92f3d193ac7aed7b9deb5a6fc78e1794f440c24a563bd185'
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