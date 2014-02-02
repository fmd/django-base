import os
import ezconf
from fabric.api import *
from fabric.colors import green, red

ezconf = ezconf.Ezconf()

def server():
    env.host_string = prompt("Deploy to server: ")
    env.user = prompt("User: ")

def _engine():
    if 'engine' in ezconf.data['db'].keys():
        default = ezconf.prompt_engine(ezconf.data['db']['engine'])
    else:
        default = ""

    engine = prompt("Database engine (mysql, postgres): ", default = default)
    ret = ezconf.deprompt_engine(engine)

    if ret is None:
        print(red("Bad database engine: " + engine))
        return False

    return ret

def _name():
    if 'name' in ezconf.data['db'].keys():
        default = ezconf.data['db']['name']
    else:
        default = ""

    name = prompt("Database name: ", default = default)
    if len(name) == 0:
        print(red("Please enter a database name."))
        return False
    return name

def _user():
    if 'user' in ezconf.data['db'].keys():
        default = ezconf.data['db']['user']
    else:
        default = ""

    username = prompt("Database username: ", default = default)
    if len(username) == 0:
        print(red("Please enter a database username."))
        return False
    return username

def _pass():
    if 'pass' in ezconf.data['db'].keys():
        default = ezconf.data['db']['pass']
    else:
        default = ""

    password = prompt("Database password: ", default = default)
    if len(password) == 0:
        print(red("Please enter a database password."))
        return False
    return password

def _debug():
    if 'debug' in ezconf.data['env'].keys():
        default = ezconf.prompt_bool(ezconf.data['env']['debug'])
    else:
        default = ""

    d = prompt("Deploy with debug mode on? (y/n): ", default = default)
    ret = ezconf.deprompt_bool(d)
    if ret is None:
        print(red("Please choose 'y' or 'n'."))
        return None

    return ret

def _proj_name():
    if 'name' in ezconf.data['project'].keys():
        default = ezconf.data['project']['name']
    else:
        default = ""

    name = prompt("Project name: ", default = default)
    if len(name) == 0:
        print(red("Please enter a project name."))
        return False
    return name

def config():
    env.PROJECT_NAME = None
    while env.PROJECT_NAME is None:
        env.PROJECT_NAME = _proj_name()
    ezconf.data['project']['name'] = env.PROJECT_NAME

    env.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    ezconf.data['project']['base_dir'] = env.BASE_DIR

    env.PROJECT_DIR = os.path.dirname(env.BASE_DIR + "/" + env.PROJECT_NAME + "/") 
    ezconf.data['project']['project_dir'] = env.PROJECT_DIR
    
    env.DEBUG = None
    while env.DEBUG is None:
        env.DEBUG = _debug()
    ezconf.data['env']['debug'] = env.DEBUG

    env.DB_ENGINE = False
    while not env.DB_ENGINE:
        env.DB_ENGINE = _engine()
    ezconf.data['db']['engine'] = env.DB_ENGINE

    env.DB_NAME = False
    while not env.DB_NAME:
        env.DB_NAME = _name()
    ezconf.data['db']['name'] = env.DB_NAME

    env.DB_USER = False
    while not env.DB_USER:
        env.DB_USER = _user()
    ezconf.data['db']['user'] = env.DB_USER

    env.DB_PASS = False
    while not env.DB_PASS:
        env.DB_PASS = _pass()
    ezconf.data['db']['pass'] = env.DB_PASS

    ezconf.save()

def load_config():
    env.PROJECT_NAME = ezconf.data['project']['name']
    env.BASE_DIR = ezconf.data['project']['base_dir']
    env.PROJECT_DIR = ezconf.data['project']['project_dir']
    env.DEBUG = ezconf.data['env']['debug']
    env.DB_ENGINE = ezconf.data['db']['engine']
    env.DB_NAME = ezconf.data['db']['name']
    env.DB_USER = ezconf.data['db']['user']
    env.DB_PASS = ezconf.data['db']['pass']

def migrate():
    with lcd(env.BASE_DIR):
        run("python manage.py migrate")

def createdb():
    with lcd(env.BASE_DIR):
        run("createdb " + env.PROJECT_NAME)

def local():
    env.host_string = "127.0.0.1"
    load_config()
