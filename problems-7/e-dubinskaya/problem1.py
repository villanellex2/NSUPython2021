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
        # поскольку критерий "философости" статьи нам не дан я придумала своё нелепое условие
        if bodyContent[0].text.find("философия") != -1 or bodyContent[0].text.find("философски") != -1:
            print("Статья о философии!")
            exit()

        html = bs4.BeautifulSoup(str(bodyContent), "html.parser")

        images = html.find_all('div', class_="thumb tright")
        navigation = html.find('div', class_="navbox")
        no_wiki_links = html.find_all('span', class_="citation no-wikidata")
        incorrect_links = []
        if navigation is not None:
            incorrect_links = incorrect_links + list(navigation.find_all('a', href=True))
        for div in list(images)+list(no_wiki_links):
            incorrect_links = incorrect_links + (list(div.find_all('a', href=True)))

        for link in html.find_all('a', href=True):
            if str(link['href']).find("redlink=1") == -1 and str(link).find("title") != -1 \
                    and str(link).find("class=\"") == -1 and not any(x == link for x in incorrect_links):
                if dict.get(str(link['href'])) is not None:
                    print("Oh no, links are looped, theorem doesn't work =(.")
                    exit()
                request = make_link(str(link['href']))
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