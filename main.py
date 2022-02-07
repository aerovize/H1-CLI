import sys
from colorama import init, Fore, Style
from h1 import H1

h1 = H1()


def getPrograms(page):
    # Fetches all programs and lists the companies name and handle.
    # Acme Co --> Handle: acme
    data = h1.http_get_Programs(page)
    data = data["data"]
    if data:
        # Loop through the data from the endpoint and print out each program.
        for d in data:
            print(
                Fore.WHITE + f'{d["attributes"]["name"]} --> Handle: {d["attributes"]["handle"]}')  # Acme Co --> Handle: acme
        # Check to see if the pagination needs to continue.
        next = input(Fore.YELLOW + "[*] Next Page? -> y or n: \n")
        # User either types y or n
        # if the user enters y the call the endpoint again with the second page number.
        if next == "y":
            page += 1
            h1.http_get_Programs(page)
        else:
            sys.exit(0)
    else:
        # When there are no more pages of results.
        print(Fore.RED + "[!] Last Page")


def getProgram(program_name):
    # Fetch a single program by name
    data = h1.http_get_program(program_name)
    name = data["attributes"]["name"]
    handle = data["attributes"]["handle"]
    # Access the data to get out all assets that are listed as "In Scope"
    # Prints the company name and handle
    # Followed by each assets name, type(subdomain, app, executable, code base), and info
    # Name: Acme Corp, Handle: acme
    # Asset: acme.com
    # Type: URL
    # Info: The main acme domain
    scopes = data["relationships"]["structured_scopes"]["data"]
    print(Fore.WHITE + f"\n[*] Name: {name}, Handle: {handle}\n")
    for ss in scopes:
        identifier = ss["attributes"]["asset_identifier"]
        asset_type = ss["attributes"]["asset_type"]
        info = ss["attributes"]["instruction"]
        print(f"[*] Asset: {identifier}")
        print(f"[*] Type: {asset_type}")
        print(f"[*] Info: {info}\n")


def main():
    init()  # initialize colorama
    # Prompt the user to enter either 1 to list all programs or 2 to search
    # a individual program.
    print(Fore.WHITE + "HackerOne API Client \n")
    print(Fore.WHITE + "Options:\n")
    print(Fore.WHITE + "[1] Query a list of all programs\n")
    print(Fore.WHITE + "[2] Seach for a specific program\n")
    option = input(Fore.YELLOW + "[?] => ")
    if option == "1":
        page = 1
        getPrograms(page)
    elif option == "2":
        # If searching for an individual program
        # the name is required.
        program_name = input(
            Fore.YELLOW + "[?] Please enter a program handle: ")
        getProgram(program_name)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
