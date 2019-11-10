#!/usr/bin/env python3
import json,sys
from flask import Flask

SETTINGS_FILE = "settings.json"
MESSAGES_FILE = "messages.json"

## CONFIG GLOBAL VALUES ##
SERVER_PORT = ""

def main():
    init_settings()

def init_settings():
    with open(globals()["SETTINGS_FILE"],"r") as settings_file:
        json_settings = json.load(settings_file)
        
        ## OVERWRITING GLOBAL SETTINGS CONFIG ##
        globals()["SERVER_PORT"] = json_settings["SERVER_PORT"]


if __name__ == "__main__":
    main()