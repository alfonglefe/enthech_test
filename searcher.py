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
        print(url)
        response = requests.get(url, headers=headers)

        htmlText = BeautifulSoup(response.text, "html.parser")
        results = htmlText.find("ol").find_all("li", class_="b_algo")

        for i in range(len(results)):
            title = results[i].find("h2").find("a").text
            url = results[i].find("h2").find("a")["href"]
            description = results[i].find("p").text
            itemsSearched.append(SearchItem(title, description, url))

    write_to_file(f"Busquedas_{searchTerm}", itemsSearched)

def search_with_list(parametersList):
    if len(parametersList) == 1:
        search_and_save(parametersList[0])
    elif len(parametersList) == 3:
        search_and_save(parametersList[0], parametersList[1], parametersList[2])
    elif len(parametersList) == 2:
        if isinstance(parametersList[1], str):
            search_and_save(parametersList[0], fileType=parametersList[1])
        else:
            search_and_save(parametersList[0], pagesToSearch=parametersList[1])

def main():
    search_and_save("enthec")
    search_and_save("test", fileType="pdf")
    search_with_list(["lista", "doc", 2])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
