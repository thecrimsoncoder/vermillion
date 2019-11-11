#!/usr/bin/env python3
import json,sys
from flask import Flask

SETTINGS_FILE = "settings.json"


## CONFIG GLOBAL VALUES ##
SERVER_PORT = ""
MESSAGES_FILE = ""
API_KEYS_FILE = ""

def main():
    init_settings()

def init_settings():
    with open(globals()["SETTINGS_FILE"],"r") as settings_file:
        json_settings = json.load(settings_file)
        
        ## OVERWRITING GLOBAL SETTINGS CONFIG ##
        globals()["SERVER_PORT"] = json_settings["SERVER_PORT"]
        globals()["MESSAGES_FILE"] = json_settings["MESSAGES_FILE"]
        globals()["API_KEYS_FILE"] = json_settings["API_KEYS_FILE"]


if __name__ == "__main__":
    main()