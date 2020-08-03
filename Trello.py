import requests
import json
import os 

class Trello:
    def __init__(self):
        self.key = os.environ['key']
        self.token = os.environ['token']