from constants import *
import requests

def init_board():
    for l in LISTS:
        url = BASE_URL + f'/lists?name={l}&idBoard={ID_BOARD}'
        requests.request('POST', url, params=AUTH)
    for label in LABELS:
        url = BASE_URL + f'/boards/{ID_BOARD}/labels?name={label[0]}&color={label[1]}'
        requests.request('POST', url, params=AUTH)
    
  
if __name__ == '__main__':
    init_board()