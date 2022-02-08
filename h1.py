import os
import requests
from dotenv import load_dotenv

load_dotenv()


class H1:
    def __init__(self) -> None:
        self.token = os.getenv("TOKEN")
        self.username = os.getenv("USERNAME")
        self.header = {
            'Accept': 'application/json'
        }

    def http_get_Programs(self, page):
        # Make a get request to the API and fecth all programs
        # the user has access to.
        # Requires a page number for pagination
        # https://api.hackerone.com/v1/hackers/programs/?page[number]=1&page[size]=100
        try:
            resp = requests.get(f'https://api.hackerone.com/v1/hackers/programs/?page[number]={page}&page[size]=100', auth=(
                self.username, self.token), headers=self.header)
            return resp.json()
        except ConnectionError as err:
            print(err)
            return err

    def http_get_program(self, program_handle):
        # Make a get reguest to the API to fetch a single program.
        # Requires the handle name of the program
        # https://api.hackerone.com/v1/hackers/programs/acme
        try:
            resp = requests.get(f'https://api.hackerone.com/v1/hackers/programs/{program_handle}',
                                auth=(self.username, self.token), headers=self.header)
            return resp.json()
        except requests.exceptions.HTTPError:
            # if a invalid handle is entered, we will not get a 200 status code
            # so return the status code.
            return resp.status_code
