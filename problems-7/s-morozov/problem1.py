#!/usr/bin/env python3

from io import BytesIO
import requests
from lxml import etree, html
import urllib.parse
import time
import tldextract
import sys

wikipedia_prefix = 'https://{}.wikipedia.org/'
random_url = 'https://en.wikipedia.org/wiki/Special:Random'
philosophy_url = 'https://en.wikipedia.org/wiki/Philosophy'

if len(sys.argv) == 1:
    url = random_url
else:
    url = sys.argv[1]


def clear_tag(tree):
    allowed_tags = ['a', 'p', 'b', 'ul', 'ol', 'li']
    for el in tree.getchildren():
        if el.tag not in allowed_tags:
            el.drop_tree()
        else:
            clear_tag(el)


def get_heading(tree):
    el = tree.get_element_by_id('firstHeading')
    etree.strip_tags(el, 'i')
    return el.text


def find_text_in_parentheses(text):
    res = []
    cur = ''
    depth = 0
    for ch in text:
        if ch in ')）':
            depth -= 1
            if depth == 0:
                cur += ch
                res.append(cur)
                cur = ''
        elif ch in '(（':
            depth += 1
        if depth > 0:
            cur += ch
    return res


def get_first_link(tree):
    content = tree.get_element_by_id("mw-content-text")
    body = content.find_class('mw-parser-output')[0]
    clear_tag(body)

    # find all text in parentheses
    pars = find_text_in_parentheses(html.tostring(body, encoding='unicode'))

    for link_element in body.iter('a'):
        if link_element.get('class') == 'new':  # red link
            continue
        if link_element.get('href').startswith('#'):  # link to another part of the article
            continue
        in_parentheses = False
        for par in pars:
            if html.tostring(link_element, with_tail=False, encoding='unicode') in par:
                in_parentheses = True
                break
        if not in_parentheses:
            return link_element.get('href')
    return None


def is_philosophy(tree):
    links_to_en = tree.find_class('interlanguage-link interwiki-en')
    if len(links_to_en) == 0:
        return False  # no English interwiki present
    return links_to_en[0].findall('a')[0].get('href') == philosophy_url


def find_philosophy(start_url):
    visited_pages = set()
    visited_list = []  # required for cycle print
    current_url = start_url
    subdomain = tldextract.extract(current_url).subdomain
    while True:
        response = requests.get(current_url)
        tree = html.parse(BytesIO(response.content)).getroot()
        heading = get_heading(tree)
        print(f'{len(visited_pages)}: {heading} {urllib.parse.unquote(response.url)}')
        visited_list.append(heading)
        if response.url in visited_pages:
            print('Cycle found:')
            print(' -> '.join(visited_list[visited_list.index(heading):]))
            break
        visited_pages.add(response.url)
        if response.url == philosophy_url or is_philosophy(tree):
            print(f'Philosophy found in {len(visited_pages) - 1} steps')
            break
        first_link = get_first_link(tree)
        if first_link is None:
            print(f"No links in the article: {heading}")
            break
        current_url = urllib.parse.urljoin(wikipedia_prefix.format(subdomain), first_link)
        time.sleep(0.5)


find_philosophy(url)

