import argparse
import requests
from bs4 import BeautifulSoup
import sys
import urllib
import time

end_url = 'https://en.wikipedia.org/wiki/Philosophy'
random_article = 'https://en.wikipedia.org/wiki/Black_metal'

parser = argparse.ArgumentParser(description='Wikipedia: Getting to Philosophy')
parser.add_argument('-u', '--url', type=str, help='wiki article to start from')
args = parser.parse_args()

if args.url:
    start_url = args.url
else:
    start_url = random_article


def get_first_link(url: str) -> str:
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    first_article_url = None

    # Тела статей на википедии лежат вот здесь
    article_content = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    if article_content == None:
        print("Something wrong with url: " + url, file=sys.stderr)
        exit()

    # Текст, который может содержать ссылки на статьи, лежит в тэгах <p>, <ul>, <ol>
    # В вышеперечсленных тэгах ссылки могут лежать только в якорях <a>
    # Причем ссылки на внешние источники имеют класс "external text", что облегчает задачу 
    
    # Удаляем все блоки с "мусором" - картинки, содержание и тд., остаются только вышеперечисленные тэги
    for div in article_content.find_all(['div', 'style', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'sup']):
        div.decompose()

    for a in article_content.find_all('a'):
        if a.has_attr("class"):
            continue
        if 'File:' in a.get('href'):
            continue
        if 'Help:' in a.get('href'):
            continue
            
        first_article_url = a.get('href')
        break
    
    # Строим полный url
    first_article_url = urllib.parse.urljoin('https://en.wikipedia.org/', first_article_url)
    return first_article_url


def getting_to_philosophy(url: str) -> None:
    history = []
    cycle = False
    found = False
    no_links = False

    while not cycle and not found and not no_links:
        url = get_first_link(url)
        print(url)
        if url == None:
            no_links = True
        elif url in history:
            cycle = True
        elif url == end_url:
            found = True
        else:
            history.append(url)
        time.sleep(1)
        
    if cycle:
        print('Cycle - philosophy not found')
    elif no_links:
        print('No links in article - philosophy not found')
    elif found:
        print('Philosophy found!')

getting_to_philosophy(start_url)