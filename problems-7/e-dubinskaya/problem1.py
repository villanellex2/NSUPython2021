#!/usr/bin/env python3

import requests
import bs4
import time
import validators


def make_link(inp: str) -> str:
    if inp.find("ru.wikipedia.org") == -1:
        return "https://ru.wikipedia.org/" + inp
    else:
        if inp.find("https://") == -1:
            return "https://" + inp
        else:
            return inp


dict = {}
print("Enter link on ru wiki page: ", end='')
request = input()

while not validators.url(request) and request.find("https://ru.wikipedia.org/") != -1:
    print("Enter link on ru wiki page: ", end='')

    request = input()

isFound = False
while True:
    response = requests.get(request)

    if response.status_code == 200:
        html = bs4.BeautifulSoup(response.text, "html.parser")
        bodyContent = html.select("#mw-content-text")

        if html.find('h1', class_="firstHeading").text == "Философия":
            print("Статья о философии!")
            exit()

        html = bs4.BeautifulSoup(str(bodyContent), "html.parser")

        images = html.find_all('div', class_="thumb tright")
        navigation = html.find('div', class_="navbox")
        infobox = html.find_all('table', class_="infobox")
        hatnote = html.find_all('div', class_="hatnote noprint dabhide")
        hatnote2 = html.find_all('div', class_="hatnote dabhide")
        dablink = html.find_all('div', class_="dablink")
        metadata = html.find('table', class_="plainlinks metadata ambox ambox-content")
        nav_tables = html.find_all('table')
        no_wiki_links = html.find_all('span', class_="citation no-wikidata")
        incorrect_links = []

        for table in nav_tables:
            if table.decomposed is not False and table.has_attr("class") and str(table.get("class")).find("navbox") != -1:
                table.decompose()

        for div in list(hatnote) + list(infobox) + list(hatnote2) + list(dablink):
            div.decompose()
        for div in list(images) + list(no_wiki_links):
            div.decompose()
        if navigation is not None:
            navigation.decompose()
        if metadata is not None:
            metadata.decompose()
        for link in html.find_all('a', href=True):
            if str(link['href']).find("redlink=1") == -1 and str(link).find("title") != -1:
                if dict.get(str(link['href'])) is not None:
                    print("Oh no, links are looped, theorem doesn't work =(, next link is " + link['title'])
                    exit()
                request = make_link(str(link['href']))
                parent = link.parent
                while parent is not None:
                    parent = parent.parent
                link_title = str(link['title'])
                isFound = True
                print("Follow the link \"" + link_title + "\": " + request)
                dict[str(link['href'])] = 0
                break

        if not isFound:
            print("No correct links on the page, theorem doesn't work =(.")
            exit()
        else:
            isFound = False
            time.sleep(1.5)
    else:
        import stderr

        print("Status code = " + str(request.status_code), file=stderr)
