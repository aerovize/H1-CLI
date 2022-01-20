import sys
import requests

from colorama import init, Fore, Style

req = {
    "headers": {
        'Accept': 'application/json'
    },
    "api": 'https://api.hackerone.com/v1/hackers/programs'
}

# Fetches all programs that user has access to


def getPrograms(page):
    try:
        resp = requests.get(f'{req["api"]}/?page[number]={page}&page[size]=100', auth=('H1-USERNAME', 'API-KEY'), headers=req["headers"]
                            )
        data = resp.json()
        data = data["data"]
        if data:
            for d in data:
                print(
                    Fore.WHITE + f'{d["attributes"]["name"]} --> Handle: {d["attributes"]["handle"]}')
            next = input(Fore.YELLOW + "[*] Next Page? -> y or n: \n")
            if next == "y":
                page += 1
                getPrograms(page)
            else:
                sys.exit()
        else:
            print(Fore.RED + "[!] Last Page")
    except:
        sys.exit(1)

# Fetches a single program


def getProgram(program_name):
    try:

        resp = requests.get(f'{req["api"]}/{program_name}', auth=('H1-USERNAME',
                            'API-KEY'), headers=req["headers"])
        data = resp.json()
        name = data["attributes"]["name"]
        handle = data["attributes"]["handle"]

        scopes = data["relationships"]["structured_scopes"]["data"]
        print(Fore.WHITE + f"\n[*] Name: {name}, Handle: {handle}\n")
        for ss in scopes:
            identifier = ss["attributes"]["asset_identifier"]
            asset_type = ss["attributes"]["asset_type"]
            info = ss["attributes"]["instruction"]
            print(f"[*] Asset: {identifier}")
            print(f"[*] Type: {asset_type}")
            print(f"[*] Info: {info}\n")
    except:
        sys.exit(1)


def main():
    init()
    print(Fore.WHITE + "HackerOne API Client \n")
    print(Fore.WHITE + "Options:\n")
    print(Fore.WHITE + "[1] Query a list of all programs\n")
    print(Fore.WHITE + "[2] Seach for a specific program\n")
    option = input(Fore.YELLOW + "[?] => ")
    if option == "1":
        page = 1
        getPrograms(page)
    elif option == "2":
        program_name = input(
            Fore.YELLOW + "[?] Please enter a program handle: ")
        getProgram(program_name)
    else:
        sys.exit()


if __name__ == '__main__':
    main()
