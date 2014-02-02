import os
import json
from pprint import pprint

class Ezconf():
    def __init__(self):
        try:
            self.load()
        except:
            self.data = {
                'project': {

                },

                'env': {

                },

                'db': {

                },
            }

    def load(self, file = "config.json"):
        handle = open(file)
        self.data = json.load(handle)
        pprint(self.data)
        handle.close()

    def save(self, file = "config.json"):
        with open("config.json", 'w') as handle:
            json.dump(self.data, handle)

    def prompt(self, p):
        if p is True:
            return 'y'

        if p is False:
            return 'n'

        return p

    def deprompt(self, p): 
        if p == 'y':
            return True
        if p == 'n':
            return False

        return p