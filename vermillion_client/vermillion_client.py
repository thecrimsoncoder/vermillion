#!/usr/bin/env python3
import os,sys,requests\
from rotor import Rotor

API_KEY_FILE = "api_keys.json"

def main():
    return True

def title():
    print("    ▄   ▄███▄   █▄▄▄▄ █▀▄▀█ ▄█ █    █    ▄█ ████▄    ▄   ")
    print("     █  █▀   ▀  █  ▄▀ █ █ █ ██ █    █    ██ █   █     █  ")
    print("█     █ ██▄▄    █▀▀▌  █ ▄ █ ██ █    █    ██ █   █ ██   █ ")
    print(" █    █ █▄   ▄▀ █  █  █   █ ▐█ ███▄ ███▄ ▐█ ▀████ █ █  █ ")
    print("  █  █  ▀███▀     █      █   ▐     ▀    ▀ ▐       █  █ █ ")
    print("   █▐            ▀      ▀                         █   ██ ")
    print("   ▐                                                     ")
    print("   Created by Sean McElhare | github.com/thecrimsoncoder ")
    print("\n")


def menu():
    helper_selected_api_key()
    print("+-------------------------------------------------------+")
    print("| 1. Create Message                                     |")
    print("| 2. Decode Message                                     |")
    print("| 3. Add API Key                                        |")
    print("| 4. Select API Key                                     |")
    print("| 5. Remove API Key                                     |")
    print("| 6. Exit                                               |")
    print("+-------------------------------------------------------+")
    print("\n")
    opt = input("[OPTION]: ")

    if opt == "1"
        if message_handler("create") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "2"
        if message_handler("decode") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "3":
        if api_key_handler("add") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "4":
        if api_key_handler("select") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "5":
        if api_key_handler("destroy") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "6":
        print("") ## TODO
        sys.exit(0)
    else:
        print("") ## TODO
        time.sleep(2)
        menu()

def message_handler(cmd):
    if cmd == "create":
        try:
        except Exception as err:
            print(err)
            return False

    elif cmd == "decode":
        try:
        except Exception as err:
            print(err)
            return False

    else:
        return False

def api_key_handler(cmd):
    if cmd == "add":
        try:
        except Exception as err:
            print(err)
            return False

    elif cmd == "select":
        try:
        except Exception as err:
            print(err)
            return False

    elif cmd == "destroy":
        try:
        except Exception as err:
            print(err)
            return False
    else:
        return False

def helper_selected_api_key():
    return True
    
if __name__ == "__main__":
    main()