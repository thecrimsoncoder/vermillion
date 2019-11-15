#!/usr/bin/env python3
import os,json,time,sys,hashlib,datetime
from subprocess import Popen, PIPE

SETTINGS_FILE = "settings.json"

## GLOBALS - Defined in init_settings() ##
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
    print("   Created by Sean McElhare | github.com/thecrimsoncoder ")
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
    print("| 8. Clean up inactive API Keys (active : False)        |")
    print("| 9. Exit                                               |")
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
        if api_key_handler("list") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "4":
        if api_key_handler("create") ==  True:
            menu()
        else:
            print("") ## TODO
    elif opt == "5":
        if api_key_handler("activate") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "6":
        if api_key_handler("deactivate") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "7":
        if api_key_handler("destroy") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "8":
        if api_key_handler("cleanup") == True:
            menu()
        else:
            print("") ## TODO
    elif opt == "9":
        print("") ## TODO
        sys.exit(0)
    else:
        print("") ## TODO
        time.sleep(2)
        menu()

def server_handler(server_cmd):

    if str(server_cmd) == "start":
        cmd = "" ## TODO

    elif str(server_cmd) == "stop":
        cmd = "" ## TODO

    try:
        server_handler = Popen(cmd,stdout="PIPE",stderr="PIPE",shell=True)
        (cmd_output,cmd_err) = server_handler.communicate()
        cmd_rc = server_handler.poll()

        if cmd_rc == 0:
            print("[INFO] " + str(cmd_output))
            return True
        else:
            print(str(cmd_err))
            return False
    except Exception as err:
        print(err)
        return False

def api_key_handler(cmd):
    if cmd == "list":
        try:
            with open(API_KEYS_FILE, "r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                print("---------------------------------------------------------------------------------------------")
                for api_key in api_keys:
                    print("Key: " + str(api_key['api_key']))
                    print("Description: " + str(api_key['description']))
                    print("Active: " + str(api_key['active']))
                    print("---------------------------------------------------------------------------------------------")
            return True
        except Exception as err:
            print(err)
            return False
            
    elif cmd == "create":
        try:
            with open("/etc/machine-id","r") as file_handler:
                system_uuid = file_handler.read() ## Grabbing UUID of system set at install time
                file_handler.close()

            encoded_key = (str(time.time())+str(system_uuid)).encode()
            api_token = hashlib.sha256(encoded_key).hexdigest()
            api_token_description = input("API KEY DESCRIPTION: ")

            api_key = {
                "api_key" : str(api_token),
                "active" : False,
                "description" : str(api_token_description)
            }

            with open(API_KEYS_FILE,"r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                api_keys.append(api_key)

            with open(API_KEYS_FILE,"w") as api_key_database:
                json.dump(api_keys,api_key_database, indent=4, separators=(',', ' : '))
                api_key_database.close()

            print("\n")
            print("---------------------------------------------------------------------------------------------")
            print("[API_KEY]     " + str(api_token) + "     [API_KEY]")
            print("---------------------------------------------------------------------------------------------")
            print("[INFO] Copy this key and distribute to a client")
            print("[INFO] This key will need to be ACTIVATED before use!")
            print("\n")
            return True

        except Exception as err:
            print(err)
            return False

    elif cmd == "activate":
        try:
            with open(API_KEYS_FILE, "r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                print("---------------------------------------------------------------------------------------------")
                for api_key in api_keys:
                    print("Key: " + str(api_key['api_key']))
                    print("Description: " + str(api_key['description']))
                    print("Active: " + str(api_key['active']))
                    print("---------------------------------------------------------------------------------------------")
                activate_key = input("Paste the key you would like to activate: ")
                if len(activate_key) == 64 and helper_search_for_key(str(activate_key)) == True:
                    for api_key in api_keys:
                        if api_key['api_key'] == str(activate_key):
                            api_key['active'] =  True
                            break
                    with open(API_KEYS_FILE, "w") as api_key_database:
                        json.dump(api_keys,api_key_database, indent=4, separators=(',', ' : '))
                        api_key_database.close()
                else:
                    print("Please enter a valid api key...")
                    time.sleep(2)
            return True
        except Exception as err:
            print(err)
            return False

    elif cmd == "deactivate":
        try:
            with open(API_KEYS_FILE, "r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                print("---------------------------------------------------------------------------------------------")
                for api_key in api_keys:
                    print("Key: " + str(api_key['api_key']))
                    print("Description: " + str(api_key['description']))
                    print("Active: " + str(api_key['active']))
                    print("---------------------------------------------------------------------------------------------")
                deactivate_key = input("Paste the key you would like to deactivate: ")
                if len(deactivate_key) == 64 and helper_search_for_key(str(deactivate_key)) == True:
                    for api_key in api_keys:
                        if api_key['api_key'] == str(activate_key):
                            api_key['active'] =  False
                            break
                    with open(API_KEYS_FILE, "w") as api_key_database:
                        json.dump(api_keys,api_key_database, indent=4, separators=(',', ' : '))
                        api_key_database.close()
                else:
                    print("Please enter a valid api key...")
                    time.sleep(2)
            return True
        except Exception as err:
            print(err)
            return False

    elif cmd == "destroy":
        try:
            with open(API_KEYS_FILE, "r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                print("---------------------------------------------------------------------------------------------")
                for api_key in api_keys:
                    print("Key: " + str(api_key['api_key']))
                    print("Description: " + str(api_key['description']))
                    print("Active: " + str(api_key['active']))
                    print("---------------------------------------------------------------------------------------------")
                destroy_key = input("Paste the key you would like to remove: ")
                if len(destroy_key) == 64 and helper_search_for_key(str(destroy_key)) == True:
                    for api_key in api_keys:
                        if api_key['api_key'] == str(destroy_key):
                            api_keys.remove(api_key)
                            break
                    with open(API_KEYS_FILE, "w") as api_key_database:
                        json.dump(api_keys,api_key_database, indent=4, separators=(',', ' : '))
                        api_key_database.close()
                else:
                    print("Please enter a valid api key...")
                    time.sleep(2)
            return True
        except Exception as err:
            print(err)
            return False

    elif cmd == "cleanup":
        active_keys = []
        try:
            with open(API_KEYS_FILE, "r") as api_key_database:
                api_keys = json.load(api_key_database)
                api_key_database.close()
                for api_key in api_keys:
                    if api_key['active'] == True:
                        active_keys.append(api_key)
            with open(API_KEYS_FILE, "w") as api_key_database:
                json.dump(active_keys,api_key_database, indent=4, separators=(',', ' : '))
                api_key_database.close()
            return True
        except Exception as err:
            print(err)
            return False
    else:
        return False

def helper_search_for_key(search_key):
    try:
        key_found = False
        with open(API_KEYS_FILE,"r") as api_key_database:
            api_keys = json.load(api_key_database)
            api_key_database.close()
            for api_key in api_keys:
                if api_key['api_key'] == str(search_key):
                    key_found = True
                    break
        return key_found
    except Exception as err:
        print(err)
        return False

def init_settings():
    try:
        with open(globals()["SETTINGS_FILE"],"r") as settings_file:
            json_settings = json.load(settings_file)
            
            ## Defining GLOBALS ##
            globals()["API_KEYS_FILE"] = json_settings["API_KEYS_FILE"]
            return True
    except Exception as err:
        print(err)
        return False

if __name__ == "__main__":
    main()