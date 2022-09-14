from bs4 import BeautifulSoup
import requests
import re

# Asking User Preferences
# graphics = input("What kind of product are you looking for?")
graphics = 3080

# Getting the URL
url = f"https://www.newegg.ca/p/pl?d={graphics}&N=4131"

# Getting the HTML Document using BeautifulSoup
document = BeautifulSoup(requests.get(url).text , 'html.parser');

