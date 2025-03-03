import requests
from bs4 import BeautifulSoup
import re

class WikiCrawler:
    def __init__(self, max_depth):
        # the maximum depth of recursion that
        # this crawler should search to
        self.max_depth = max_depth
        self.visited = []

    def is_name(s):
        return re.match("^[A-Z][A-Za-z\-']* [A-Z][A-Za-z\-']*$", s)

    def articles_linked_from(article):
        response = requests.get(
            url="https://en.wikipedia.org/wiki/" + article,
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        allLinks = soup.find(id="bodyContent").find_all("a")
        wikiArticles = []
        for link in allLinks:
            if link.has_attr("href") and \
                    link['href'].find("/wiki/") != -1 and \
                    link.has_attr("title") and \
                    WikiCrawler.is_name(link['title']):
                wikiArticles.append(link['title'])
        return wikiArticles

    def article(article):
        response = requests.get(
            url="https://en.wikipedia.org/wiki/" + article,
        )
        return response


    def crawl(self, start, end, depth):
       # Task 2
       
       # if start and end articles are the same return true
        if start == end: 
            return True
        
        # variable holding list of all links on start page
        links_on_page = WikiCrawler.articles_linked_from(start)
        
        if end in links_on_page:
            return True
        
        elif depth >= self.max_depth:
            return False
        
        ender = False

        for each in links_on_page:
            if each not in self.visited:
                if self.crawl(each, end, 1 + depth):
                    ender = True
                    return True
                self.visited.append(each)
             
        return ender 
        
    def connected(self, start, end):
        # Task 1
    
        # Check if start and end articles are valid
        if WikiCrawler.article(start).status_code != 200 or WikiCrawler.article(end).status_code != 200:
            return False

        
        # Invoke crawl() method with start article, end article, and depth of 0
        else:
            return self.crawl(start, end, 0)
