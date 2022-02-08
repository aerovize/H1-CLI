from colorama import init, Fore

from h1 import H1


class Single_Program(H1):
    init()

    def input_error(self, message):
        # Prints a error message
        print(Fore.RED + "\n-----------------------------")
        print(Fore.RED + f"[!] {message} [!]")
        print(Fore.RED + "-----------------------------\n")

    def single_Program(self, program_name):
        # Fetch a single program by name
        data = self.http_get_program(program_name)
        if data != 200:
            # If anything other than a 200 status code comes back,
            # return to the input_handle function
            self.input_error('Please enter a valid program handle')
            self.input_handle()
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

    def input_handle(self):
        # If searching for an individual program
        # the handle name is required.
        handle = input(Fore.YELLOW + "[?] Please enter a program handle: ")

        self.single_Program(handle)
