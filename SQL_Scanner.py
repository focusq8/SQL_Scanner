import requests

Red = "\033[1;31;40m"
Blue = "\033[1;36;40m"
Yellow="\033[0;33m"

try:
    with open("words.txt", 'r') as lists:
            dictionary = lists.read().splitlines()
except FileNotFoundError:
        input("Couldn't find words.txt!")
        exit()

url =  input("Enter Your Site: ")

def mysql():
    print(f"{Yellow}database is mysql")
    try:
        for lists in dictionary:
            request = requests.get(url + lists.rstrip())
            if "mysql" in request.text:
                print(f"{Blue}[+] Found Payload: {lists}")
                with open("found Payloads.txt", 'a') as file:
                    file.write(f"{url}{lists}\n")
                    continue
            else:
                print(f"{Red}[-] Not Found Payload: {lists}")
                continue
    except Exception:
        input(f"{Yellow}[-] error !!!")

def msSQL():
    print(f"{Yellow}database is msSQL")
    try:
        for lists in dictionary:
            request = requests.get(url + lists.rstrip())
            if "Microsoft SQL" in request.text:
                print(f"{Blue}[+] Found Payload: {lists}")
                with open("found Payloads.txt", 'a') as file:
                    file.write(f"{url}{lists}\n")
                    continue
            else:
                print(f"{Red}[-] Not Found Payload: {lists}")
                continue
    except Exception:
        input(f"{Yellow}[-] error !!!")

def PostgreSQL():
    print(f"{Yellow}database is PostgreSQL")
    try:
        for lists in dictionary:
            request = requests.get(url + lists.rstrip())
            if "PostgreSQL" in request.text:
                print(f"{Blue}[+] Found Payload: {lists}")
                with open("found Payloads.txt", 'a') as file:
                    file.write(f"{url}{lists}\n")
                    continue
            else:
                print(f"{Red}[-] Not Found Payload: {lists}")
                continue
    except Exception:
        input(f"{Yellow}[-] error !!!")

def Oracle():
    print(f"{Yellow}database is Oracle")
    try:
        for lists in dictionary:
            request = requests.get(url + lists.rstrip())
            if "ORA-00933" or "Oracle" in request.text:
                print(f"{Blue}[+] Found Payload: {lists}")
                with open("found Payloads.txt", 'a') as file:
                    file.write(f"{url}{lists}\n")
                    continue
            else:
                print(f"{Red}[-] Not Found Payload: {lists}")
                continue
    except Exception:
        input(f"{Yellow}[-] error !!!")

def starter():
    try:
        for lists in dictionary:
            request = requests.get(url + lists.rstrip())
            if "mysql" in request.text:
                mysql()
            elif "Microsoft SQL" in request.text:
                msSQL()

            elif "PostgreSQL" in request.text:
                PostgreSQL()

            elif "Oracle" in request.text:
                Oracle()
            else:
                print("not payload")
    except:
        print(f"{Yellow}database is not payload")

starter()
input(f"{Yellow}Finished")