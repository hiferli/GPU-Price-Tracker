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

# Getting the Last Page Number from the list of pages
nextPages = document.find(class_ = 'list-tool-pagination-text').strong
lastPageNumber = int(str(nextPages).split('/')[-2].split(">")[-1][:-1]);
# print(lastPageNumber);

# Traversing through all the pages
for page in range(1 , lastPageNumber + 1):
    url = f"https://www.newegg.ca/p/pl?d={graphics}&N=4131&page={page}"
    pageDocument = BeautifulSoup(requests.get(url).text , 'html.parser') 

    # Div with all the Graphic Card Information
    cardsDiv = pageDocument.find(class_ = "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    # Getting info from all the contents
    cards = cardsDiv.find_all(text = re.compile(str(graphics)));

    # Traversing through all the GPUs available in the search
    for card in cards:
        cardParent = card.parent;

        if cardParent.name != 'a':
            continue;

        link = cardParent['href'];
        print(link);