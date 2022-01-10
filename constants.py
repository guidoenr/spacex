from conf import credentials as cre, workspace as wkp

WORDS = ['rands', 'w0rd', 'inheritance','another', 'simple', 'spacex', 'etc', 'pelde', 'mars', 'juno', 'pluto', 'saturn']
BASE_URL = 'https://api.trello.com/1'

# ---------------------------------- PRIVATE
ID_BOARD = cre["private"]['id_board']
TOKEN = cre["private"]['token']
API_KEY = cre["private"]['api_key']

AUTH = {
        'key': API_KEY,
        'token': TOKEN
    }

# ---------------------------------- WORKSPACE SETTINGS 
# LIST
ID_TODO_LIST = wkp["lists"]['id_todo']

# LABELS
ID_BUG_LABEL = wkp["labels"]['id_bug']
ID_ISSUE_LABEL = wkp["labels"]['id_issue']
ID_TASK_LABEL = wkp["labels"]['id_task']
ID_TEST_LABEL = wkp["labels"]['id_test']
ID_MAINTENANCE_LABEL = wkp["labels"]['id_maintenance']
ID_RESEARCH_LABEL = wkp["labels"]['id_research']

# TO_INIT
LISTS = ['Done', 'Doing', 'To Do']
LABELS = [('Bug', 'red'), ('Task', 'blue'), ('Issue', 'yellow'),
          ('Maintenance', 'green'), ('Research', 'orange'), ('Test', 'purple')]


