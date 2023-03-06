import sys

import json
import requests
import urllib.parse
from bs4 import BeautifulSoup

from models.SearchItem import SearchItem


def write_to_file(fileName, items):
    fileTxt = open(f"./outputs/{fileName}.txt", "w", encoding="utf-8")
    itemsJson = []

    for i in range(len(items)):
        fileTxt.write(items[i].__str__())
        fileTxt.write("\n")
        itemsJson.append(json.dumps(items[i].__dict__))

    fileTxt.close()

    fileJson = open(f"./outputs/{fileName}.json", "w", encoding="utf-8")
    fileJson.write(json.dumps(itemsJson))
    fileJson.close()



def search_and_save(searchTerm, fileType="", pagesToSearch=1):

    if not fileType:
        query = urllib.parse.quote(searchTerm)
    else:
        query = urllib.parse.quote(f"filetype:{fileType}")+"+"+urllib.parse.quote(searchTerm)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Referer': 'https://www.bing.com/'}

    itemsSearched = []
    for page in range(1, pagesToSearch+1):

        url = f"https://www.bing.com/search?q={query}&go=Submit&qs=n&pq={query}&first={str(10*(page-1)+1)}&FORM=PERE"
        response = requests.get(url, headers=headers)

        htmlText = BeautifulSoup(response.text, "html.parser")
        results = htmlText.find("ol").find_all("li", class_="b_algo")

        for i in range(len(results)):
            title = results[i].find("h2").find("a").text
            url = results[i].find("h2").find("a")["href"]
            description = results[i].find("p").text
            itemsSearched.append(SearchItem(title, description, url))

    write_to_file(f"Busquedas_{searchTerm}", itemsSearched)


def main():
    search_and_save("enthec", pagesToSearch=2)
    search_and_save("test", fileType="pdf")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
