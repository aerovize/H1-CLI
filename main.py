from colorama import init, Fore
from single import Single_Program
from all import All_Programs


def input_options():
    all = All_Programs()
    single = Single_Program()
    # Prompt the user to enter 1. to list all programs or 2. to search
    # a individual program.
    print(Fore.WHITE + "HackerOne API Client \n")
    print(Fore.WHITE + "Options:\n")
    print(Fore.WHITE + "[1] Query a list of all programs\n")
    print(Fore.WHITE + "[2] Seach for a specific program\n")
    option = input(Fore.YELLOW + "[?] => ")
    if option == "1":
        all.all_programs()
    elif option == "2":
        single.input_handle()
    else:
        # If the user enters the wrong input restart the script
        all.input_error('Please enter 1 or 2')
        input_options()


def main():
    init()  # initialize colorama

    input_options()


if __name__ == '__main__':
    main()
