from constants import *
import requests

def init_trello_board():
    for label in LABELS:
        base_url = BASE_URL + f'/boards/{ID_BOARD}/labels?name={label[0]}&color={label[1]}'
        requests.request('POST', base_url, params=AUTH)