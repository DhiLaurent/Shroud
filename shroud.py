import requests
import sys
import os
from urllib.parse import urlparse

print("=" * 100)
os.system("clear")
print(f"URL: {sys.argv[1]}")

def banner():
        print("\033[31m---------------------------------------------------")
        tprint(" Shroud ",font="slant")
        print("----------------------------------------------------\033[m")
from art import *
banner()



if len(sys.argv) != 3:
        # Infos
        print("\033[31m+--------------------------------------------------------+")
        print("|        How to use: python3 Shroud (URL) (Wordlist)            |")
        print("+--------------------------------------------------------+\033[m")

elif len(sys.argv) == 3:

    with open(sys.argv[2],'r', encoding='iso8859_15') as file:
        while (line := file.readline().rstrip()):
            dirs = line
            all = (sys.argv[1] + "/_/" + dirs)
            response = requests.get(all)
            if response.status_code == 200:
                parsed_url = urlparse(all)
                path = parsed_url.path
                print(f"\033[35mPage Bypassed {path}\033[m Status Code:\033[32m[{response.status_code}\033[m] ")
