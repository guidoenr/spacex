from flask import Flask, request
from model import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "github.com/guidoenr/spacex"

'''
with the .capitalize() and .globals()
methods, i would be able to create 
an instance of the desired class
using a kind of dynamic object creation ,
that will be awesome in a future, because
if there's a new "Task" i only have to create
the class
'''
@app.route("/create", methods=['POST'])
def create_task():
    json_request = request.get_json()
    _type = json_request['type'].capitalize()

    constructor = globals()[_type]
    del json_request['type']
    task_instance = constructor(**json_request)
    task_instance.create_card()

    return json_request  

if __name__ == '__main__':
    app.run()