import sys
from colorama import init, Fore

from h1 import H1


class All_Programs(H1):
    init()
    page = 1

    def input_error(self, message):
        # Prints a error message
        print(Fore.RED + "\n-----------------------------")
        print(Fore.RED + f"[!] {message} [!]")
        print(Fore.RED + "-----------------------------\n")

    def parse_data(self, all):
        data = all
        data = data["data"]
        # Loop through the data from the endpoint and print out each program.
        for d in data:
            print(
                Fore.WHITE + f'{d["attributes"]["name"]} --> Handle: {d["attributes"]["handle"]}')  # Acme Co --> Handle: acme

    def input_paginate(self):
        # Check to see if the pagination needs to continue.
        next = input(Fore.YELLOW + "[*] Next Page? -> y or n: \n")
        # User enters y or n
        # if the user enters y call the endpoint again with the second page number.
        if next == "y":
            self.page += 1
            self.http_get_Programs(self.page)
        elif next == "n":
            sys.exit(0)
        else:
            # if the user answers anything other than y or n,
            # Output error message and recall the function
            self.input_error('Please enter yes or no')
            self.input_paginate()

    def all_programs(self):

        # Fetches all programs and lists the companies name and handle.
        # Handle name is needed to fetch information about a single program
        # Acme Co --> Handle: acme

        data = self.http_get_Programs(self.page)
        if data["data"]:
            self.parse_data(data)

            self.input_paginate()
            self.all_programs()

        else:
         # When there are no more pages of results.
            print(Fore.RED + "[!] Last Page")
