from credentials import credentials as cre

BASE_URL = 'https://api.trello.com/1'

words = ['rands', 'w0rd', 'inheritance','another', 'simple', 'spacex', 'etc', 'pelde', 'mars', 'juno', 'pluto', 'saturn']

# LIST
ID_TODO_LIST = cre["lists"]['id_todo']

# PRIVATE
ID_BOARD = cre["private"]['id_board']
TOKEN = cre["private"]['token']
API_KEY = cre["private"]['api_key']
AUTH = {
        'key': API_KEY,
        'token': TOKEN
    }

# LABELS
ID_BUG_LABEl = cre["labels"]['id_bug']
ID_ISSUE_LABEl = cre["labels"]['id_issue']
ID_TASK_LABEl = cre["labels"]['id_task']
LABELS = [('Bug', 'red'), ('Task', 'blue'), ('Issue', 'yellow'),
          ('Maintenance', 'green'), ('Research', 'orange'), ('Test', 'purple')]


