import os
from fabric.api import *
from fabric.colors import green, red


def server():
    env.host_string = prompt("Deploy to server: ")
    env.user = prompt("User: ")

def _engine():
    engine = prompt("Database engine (mysql, postgres): ")
    ret = None
    if engine == "postgres":
        ret = "django.db.backends.postgresql_psycopg2"
    elif engine == "mysql":
        ret = "django.db.backends.mysql"

    if not ret:
        print(red("Bad database engine: " + engine))
        return False

    return ret

def _name():
    name = prompt("Database name: ")
    if len(name) == 0:
        print(red("Please enter a database name."))
        return False
    return name

def _user():
    username = prompt("Database username: ")
    if len(username) == 0:
        print(red("Please enter a database username."))
        return False
    return username

def _pass():
    password = prompt("Database password: ")
    if len(password) == 0:
        print(red("Please enter a database password."))
        return False
    return password

def _debug():
    d = prompt("Deploy with debug mode on? (y/n): ")
    if d == 'y':
        return True
    elif d == 'n':
        return False

    print(red("Please choose 'y' or 'n'."))
    return None

def config():
    env.conf = {}
    env.FAB_PROJECT_NAME = "djbase"
    env.conf["FAB_PROJECT_NAME"] = env.FAB_PROJECT_NAME

    env.FAB_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    env.conf["FAB_BASE_DIR"] = env.FAB_BASE_DIR

    env.FAB_PROJECT_DIR = os.path.dirname(env.FAB_BASE_DIR + "/" + env.FAB_PROJECT_NAME + "/") 
    env.conf["FAB_PROJECT_DIR"] = env.FAB_PROJECT_DIR
    
    env.FAB_DEBUG = None
    while env.FAB_DEBUG is None:
        env.FAB_DEBUG = _debug()
    env.conf["FAB_DEBUG"] = env.FAB_DEBUG

    env.FAB_DB_ENGINE = False
    while not env.FAB_DB_ENGINE:
        env.FAB_DB_ENGINE = _engine()
    env.conf["FAB_DB_ENGINE"] = env.FAB_DB_ENGINE

    env.FAB_DB_NAME = False
    while not env.FAB_DB_NAME:
        env.FAB_DB_NAME = _name()
    env.conf["FAB_DB_NAME"] = env.FAB_DB_NAME

    env.FAB_DB_USER = False
    while not env.FAB_DB_USER:
        env.FAB_DB_USER = _user()
    env.conf["FAB_DB_USER"] = env.FAB_DB_USER

    env.FAB_DB_PASS = False
    while not env.FAB_DB_PASS:
        env.FAB_DB_PASS = _pass()
    env.conf["FAB_DB_PASS"] = env.FAB_DB_PASS

def _value_string(name, value):
    v_str = ""
    if type(value) is int:
        v_str = str(value)
    elif type(value) is bool:
        v_str = str(value)
    else:
        v_str = "'" + str(value) + "'"

    return name + " = " + v_str

def local():
    env.host_string = "127.0.0.1"
    conf_file = env.FAB_PROJECT_DIR + "/generated_config.py"

    run("touch " + conf_file + " && cat /dev/null > " + conf_file)

    for name, value in env.conf.iteritems():
        print(green(name) + ": " + red(value))

        v = _value_string(name, value)

        run ("echo -e \""+ v +"\" >> "+conf_file)