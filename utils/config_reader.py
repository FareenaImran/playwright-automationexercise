import os.path
from configparser import ConfigParser


def read_config(section,key):
    config=ConfigParser()
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH=os.path.join(BASE_DIR,"..","config","config.ini")
    config.read(CONFIG_PATH)
    return config.get(section,key)