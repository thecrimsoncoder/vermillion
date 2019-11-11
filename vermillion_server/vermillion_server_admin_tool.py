#!/usr/bin/env python3
import os,json,time,sys,hashlib
from subprocess import Popen

SETTINGS_FILE = "settings.json"

API_KEYS_FILE = ""

def main():
    init_settings()
    title()
    menu()

def title():
    print("    ▄   ▄███▄   █▄▄▄▄ █▀▄▀█ ▄█ █    █    ▄█ ████▄    ▄   ")
    print("     █  █▀   ▀  █  ▄▀ █ █ █ ██ █    █    ██ █   █     █  ")
    print("█     █ ██▄▄    █▀▀▌  █ ▄ █ ██ █    █    ██ █   █ ██   █ ")
    print(" █    █ █▄   ▄▀ █  █  █   █ ▐█ ███▄ ███▄ ▐█ ▀████ █ █  █ ")
    print("  █  █  ▀███▀     █      █   ▐     ▀    ▀ ▐       █  █ █ ")
    print("   █▐            ▀      ▀                         █   ██ ")
    print("   ▐                                                     ")
    print("\n")

def menu():
    print("+-------------------------------------------------------+")
    print("| 1. Start the Server                                   |")
    print("| 2. Stop the Server                                    |")
    print("| 3. List API Keys                                      |")
    print("| 4. Generate Client API Key                            |")
    print("| 5. Activate Client API Key                            |")
    print("| 6. Deactivate Client API Key                          |")
    print("| 7. Remove an API Key                                  |")
    print("| 8. Exit                                               |")
    print("+-------------------------------------------------------+")
    print("\n")
    opt = input("[OPTION]: ")

    if opt == "1":
        if server_handler("start") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "2":
        if server_handler("stop") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "3":
        if helper_list_api_keys() == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "4":
        if api_key_handler("create") ==  True
            menu()
        else:
            print("") ## TODO
    elif opt == "5":
        if api_key_handler("activate") == True
            menu()
        else:
            print("") ## TODO
    elif opt == "6":
        if api_key_handler("deactivate") == True
            menu()
        else:
            print("") ## TODO
    elif opt == "7":
        if api_key_handler("destroy") == True
            menu()
        else:
            print("") ## TODO
    elif int(opt) == "8":
        print("") ## TODO
        sys.exit(0)
    else:
        print("") ## TODO
        time.sleep(2)
        menu()

def server_handler(server_cmd):

    if str(server_cmd) == "start":
        cmd = ""

    elif str(server_cmd) == "stop":
        cmd = ""

    server_handler = Popen(cmd,stdout="PIPE",stderr="PIPE",shell=True)
    server_handler.communicate()
    (cmd_rc,cmd_err) = server_handler.poll()

    if cmd_rc == 0:
        return True
    else:
        print(str(cmd_err))
        return False   

def api_key_handler(cmd):
    if cmd == "create":
        return True ## TODO
    elif cmd == "activate":
        return True ## TODO
    elif cmd == "deactivate":
        return True ## TODO
    elif cmd == "destroy":
        return True ## TODO
    else:
        return False

def helper_list_keys():

    with open(globals()["API_KEYS_FILE"],"r") as api_keys:
        json.dumps(api_keys)

def init_settings():
    with open(globals()["SETTINGS_FILE"],"r") as settings_file:
        json_settings = json.load(settings_file)
        
        ## OVERWRITING GLOBAL SETTINGS CONFIG ##
        globals()["API_KEYS_FILE"] = json_settings["API_KEYS_FILE"]

if __name__ == "__main__":
    main()