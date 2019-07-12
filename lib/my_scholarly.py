import scholarly

AUTHOR_QUERY = "José Miguel Horcas"

if __name__ == '__main__':
    results = scholarly.search_author(AUTHOR_QUERY)
    author = next(results).fill()
    #print(author)

    print([pub.bib['title'] for pub in author.publications])

    pub = author.publications[0].fill()
    # print(pub)
