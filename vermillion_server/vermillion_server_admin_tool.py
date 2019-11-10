#!/usr/bin/env python3
import os,json,time,sys

API_KEYS_FILE = "api_keys.json"

def main():
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
    print("| 3. Generate a Client API Key                          |")
    print("| 4. List API Keys                                      |")
    print("| 5. Remove an API Key                                  |")
    print("| 6. Exit                                               |")
    print("+-------------------------------------------------------+")
    print("\n")
    opt = input("[OPTION]: ")

    if int(opt) == 1:
        server_handler("start")
    elif int(opt) == 2:
        server_handler("stop")
    elif int(opt) == 3:
        generate_key()
    elif int(opt) == 4:
        list_keys()
    elif int(opt) == 5:
        remove_key()
    elif int(opt) == 6:
        sys.exit(0)
    else:
        print("Invalid Option")
        time.sleep(2)
        menu()

def server_handler(server_cmd):

    if str(server_cmd) == "start":
        cmd = ""

    elif str(server_cmd) == "stop":
        cmd = ""

    

def generate_key():
    return True

def list_keys():
    return True

def remove_key():
    return True

if __name__ == "__main__":
    main()