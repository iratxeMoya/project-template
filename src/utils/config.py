"""
This file loads the configuration from the config.ini file.
"""
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__) + "/../../configs/config.ini"))
