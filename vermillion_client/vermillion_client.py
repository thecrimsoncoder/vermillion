#!/usr/bin/env python3
import os,sys,requests,json
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
        msg = input("[MESSAGE]: ")
        if message_handler("create",str(msg)) == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "2"
        msg = input("[MESSAGE]: ")
        if message_handler("decode",str(msg)) == True:
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

def message_handler(cmd,msg):
    if cmd == "create":
        try: ## TODO
        except Exception as err:
            print(err)
            return False

    elif cmd == "decode":
        try: ## TODO
        except Exception as err:
            print(err)
            return False

    else:
        return False

def api_key_handler(cmd):
    if cmd == "add":
        try:
            api_key = input("Enter your API Key: ")
            vermillion_server = input("Enter the service address for this API Key: ")
            description = input("Enter a description for this API Key: ")
            if len(api_key) == 64 and vermillion_server != "" and description != "":
                if helper_search_for_key(api_key,vermillion_server) != True:
                    
                    api_key = {
                        "api_key" : str(api_key),
                        "selected" : False,
                        "vermillion_server" : str(vermillion_server),
                        "description" : str(description)
                    }

                    with open(API_KEY_FILE,"r") as api_key_database:
                        api_keys = json.load(api_key_database)
                        api_key_database.close()
                        api_keys.append(api_key)

                    with open(API_KEY_FILE,"w") as api_key_database:
                        json.dump(api_keys,api_key_database, indent=4, separators=(',', ' : '))
                        api_key_database.close()
  
                else:
                    print("[INFO] This key is already added!")
                    time.sleep(2)
                    menu()

        except Exception as err:
            print(err)
            return False

    elif cmd == "select":
        try: ## TODO
        except Exception as err:
            print(err)
            return False

    elif cmd == "destroy":
        try: ## TODO
        except Exception as err:
            print(err)
            return False
    else:
        return False

def helper_selected_api_key():
    try:
        with open(API_KEY_FILE,"r") as api_key_database:
            api_keys = json.load(api_key_database)
            api_key_database.close()

        for api_key in api_keys:
            if api_key['selected'] == True:
                return api_key
                break

    except Exception as err:
        print(err)
        return False

def helper_search_for_key(search_key,search_server):
    try:
        key_found = False
        with open(API_KEYS_FILE,"r") as api_key_database:
            api_keys = json.load(api_key_database)
            api_key_database.close()
            for api_key in api_keys:
                if api_key['api_key'] == str(search_key) and api_key['vermillion_server'] == str(search_server):
                    key_found = True
                    break
        return key_found
    except Exception as err:
        print(err)
        return False
    
if __name__ == "__main__":
    main()