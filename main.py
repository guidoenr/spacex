from flask import Flask, request
import model

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "github.com/guidoenr/spacex"

@app.route("/create", methods=['POST'])
def create_task():
    json_request = request.get_json()
    _type = json_request['type']
    print(_type)
    return json_request  


if __name__ == '__main__':
    app.run()