import unittest
from wiki_crawler import WikiCrawler

class TestWikiCrawler(unittest.TestCase):

    #
    # Testing connected() invalid cases.
    #

    # def test_connected_start_not_name(self):
    #     crawler = WikiCrawler(6)
    #     assert not crawler.connected("Global city", "Kevin Bacon")

    # def test_connected_invalid_end(self):
    #     crawler = WikiCrawler(6)
    #     assert not crawler.connected("Kevin Bacon", "Global city")

    def test_connected_invalid_start(self):
        crawler = WikiCrawler(6)
        assert not crawler.connected("Dom Cruise", "Kevin Bacon")

    def test_connected_invalid_end(self):
        crawler = WikiCrawler(6)
        assert not crawler.connected("Kevin Bacon", "Dom Cruise")

    #
    # Testing connected() valid cases.
    #

    def test_connected_direct(self):
        # should return fairly quickly
        crawler = WikiCrawler(6)
        assert crawler.connected("Kevin Bacon", "Kyra Sedgwick")

    def test_connected_close(self):
        # should return moderately quickly
        crawler = WikiCrawler(6)
        assert crawler.connected("Kevin Bacon", "Alec Baldwin")

    def test_connected_far(self):
        # should return after a couple of minutes (before Task 3)
        crawler = WikiCrawler(6)
        assert crawler.connected("Kevin Bacon", "Norah Jones")

    #
    # Tests of starter code.
    #

    def test_is_name(self):
        assert WikiCrawler.is_name("Chiwetel Ejiofor")
        assert WikiCrawler.is_name("Lupita Nyong'o")
        assert WikiCrawler.is_name("Adewale Akinnuoye-Agbaje")
        assert not WikiCrawler.is_name("Carmen Elizabeth Ejogo") # three strings (false negative)
        assert not WikiCrawler.is_name("Accra") # one string
        assert not WikiCrawler.is_name("Global city") # incorrect capitalization

    def test_article(self):
        assert WikiCrawler.article("Global city").status_code == 200
        assert WikiCrawler.article("Global xity").status_code != 200
