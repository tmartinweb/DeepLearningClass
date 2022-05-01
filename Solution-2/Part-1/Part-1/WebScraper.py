import requests
from bs4 import BeautifulSoup


class WebScraper:

    page_url = 'https://en.wikipedia.org/wiki/Machine_learning'

    def __init__(self):
        self.run_scraper()

    def __str__(self):
        print(self)

    def run_scraper(self):
        html = requests.get(WebScraper.page_url)
        page = BeautifulSoup(html.content, "html.parser")
        # Print title of page
        print(page.title.tostring)

        # Find all the links in the page ('a' tag),
        # then iterate over each tag then return the link using attribute 'href' using get
        for link in page.findAll('a'):
            print(link.get('href'))
