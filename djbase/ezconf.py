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
        handle.close()

    def save(self, file = "config.json"):
        with open("config.json", 'w') as handle:
            json.dump(self.data, handle, indent=4)

    def prompt_engine(self, p):
        if p == "django.db.backends.postgresql_psycopg2":
            return "postgres" 
        elif p == "django.db.backends.mysql":
            return "mysql"

        return p

    def deprompt_engine(self, p):
        if p == "postgres":
            return "django.db.backends.postgresql_psycopg2"
        elif p == "mysql":
            return "django.db.backends.mysql"

        return None

    def prompt_bool(self, p):
        if p is True:
            return 'y'

        if p is False:
            return 'n'

        return p

    def deprompt_bool(self, p): 
        if p == 'y':
            return True
        if p == 'n':
            return False

        return None