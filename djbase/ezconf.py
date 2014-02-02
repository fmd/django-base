import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Ezconf():
    def __init__(self):
        self.skel_data = {
            'cache': {
                'backend':'',
                'location':'127.0.0.1:11211',
            },

            'project': {
                'name':'',
                'base_dir':'',
                'project_dir':''
            },

            'env': {
                'debug':None
            },

            'db': {
                'engine':'',
                'user':'',
                'name':'',
                'pass':''
            },
        }

        try:
            self.load()
        except:
            self.data = self.skel_data

    def clear_config(self):
        self.data = self.skel_data
        self.save()

    def load(self, file = "config.json"):
        file = BASE_DIR + "/" + file
        
        handle = open(file)
        self.data = json.load(handle)
        handle.close()

    def save(self, file = "config.json"):
        file = BASE_DIR + "/" + file

        with open(file, 'w') as handle:
            json.dump(self.data, handle, indent=4)

    def prompt_engine(self, p):
        if p == "django.db.backends.postgresql_psycopg2":
            return "postgres"
        elif p == "django.db.backends.mysql":
            return "mysql"

        return ""

    def deprompt_engine(self, p):
        if p == "postgres":
            return "django.db.backends.postgresql_psycopg2"
        elif p == "mysql":
            return "django.db.backends.mysql"

        return None

    def prompt_cache(self, p):
        if p == "django.core.cache.backends.memcached.MemcachedCache":
            return "memcached"
        return ""

    def deprompt_cache(self, p):
        if p == "memcached":
            return "django.core.cache.backends.memcached.MemcachedCache"
        return None

    def prompt_bool(self, p):
        if p is True:
            return 'y'

        if p is False:
            return 'n'

        return ''

    def deprompt_bool(self, p): 
        if p == 'y':
            return True

        if p == 'n':
            return False

        return None