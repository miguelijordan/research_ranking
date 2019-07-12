# -*- coding: utf-8 -*-

import requests
import json
import argparse
import bibtexparser

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
HEADERS = {'User-Agent': USER_AGENT}
#
# NAME = "DBLP"
# URL = "https://dblp.uni-trier.de/"
#
# PID = "https://dblp.org/pid/"


EXAMPLE_BIBTEX = 'https://dblp.org/pid/142/9275'
EXAMPLE_NAME = 'Jose Miguel Horcas'


def search_author(query: str, max_results: int=1000, page: int=0) -> list:
    """Search for authors in DBLP.

    Args:
        query: Name of the author.

    Returns:
        A list of authors' names.

    """
    url = 'http://dblp.org/search/author/api?q=' + query + '&format=json&h=' + str(max_results) + '&f=' + str(page)
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print('Error "search_autor". Status code: ' + str(r.status_code))
        return []

    data = r.json()
    # print(json.dumps(data, indent=2, sort_keys=True))
    hits = data['result']['hits']
    n_results = int(hits['@sent'])
    if n_results == 0:
        return []

    # Extract author's name and id (url)
    authors = []
    for hit in hits['hit']:
        author_name = hit['info']['author']
        author_url = hit['info']['url']
        # print(">name: " + author_name)
        # print(">url: " + author_url)

        author_alias = ""
        if 'aliases' in hit['info']:
            author_alias = hit['info']['aliases']['alias']
            # print(">alias: " + str(author_alias))

        # print("---")
        author = {'name':author_name, 'alias':author_alias, 'url':author_url}
        authors.append(author)

    # Pagination
    if n_results == max_results:
        next_authors = search_author(query, max_results, page+max_results)
        authors += next_authors

    return authors

def get_publications(author_name: str, max_results: int=1000, page: int=0) -> json:
    """Search for publications of an author in DBLP.

    Returns:
        A list of publications of the author.

    """
    url = 'http://dblp.org/search/publ/api?q=author:' + author_name + ':&format=json&h=' + str(max_results) + '&f=' + str(page) + '&format=json'
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print('Error "search_publication". Status code: ' + str(r.status_code))
        return []

    data = r.json()
    # print(json.dumps(data, indent=2, sort_keys=True))
    hits = data['result']['hits']
    n_results = int(hits['@sent'])
    if n_results == 0:
        return []


    publications = []
    for hit in hits['hit']:
        # print("---------------")
        doi, title, year, type, venue = None, None, None, None, None
        if 'ee' in hit['info']:
            doi = hit['info']['ee']
        if 'title' in hit['info']:
            title = hit['info']['title']
        if 'year' in hit['info']:
            year = hit['info']['year']
        if 'type' in hit['info']:
            type = hit['info']['type']
        if 'venue' in hit['info']:
            venue = hit['info']['venue']
        if 'authors' in hit['info']:
            authors = hit['info']['authors']['author']

        # print((doi, title, year, type, venue, authors))

        pub = {'doi': doi, 'title': title, 'year': year, 'type': type, 'venue': venue, 'authors': authors}
        publications.append(pub)

    # Pagination
    if n_results == max_results:
        next_publications = get_publications(author_name, max_results, page+max_results)
        publications += next_publications

    return publications

def get_publications_bitex(author_url):
    author_url = author_url + '.bib'
    r = requests.get(author_url)
    if r.status_code != requests.codes.ok:
        print('Error "get_publications". Status code: ' + str(r.status_code))
        return []

    data = r.content
    # with open('bibtex.bib', 'w') as bibtex_file:
    #     bibtexparser.dump(data, bibtex_file)
    #
    db = bibtexparser.loads(data)
    mydata = db.get_entry_list()
    return mydata

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""DBLP search API."""
    )

    # parser.add_argument('-a', '--author', help='search for an author',  dest='author')
    # args = parser.parse_args()
    # author = args.author
    #
    # authors = search_author(author)
    # for a in authors:
    #     print("Author: " + str(a))

    #pubs = get_publications(EXAMPLE_BIBTEX)
    pubs = get_publications(EXAMPLE_NAME)
    for p in pubs:
        print(p)
        print("------------------")
