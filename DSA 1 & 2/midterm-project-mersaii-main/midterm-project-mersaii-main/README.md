# Wiki Crawler

For this midterm project, you will implement a recursive Web crawler for [wikipedia.com](wikipedia.com). The crawler will allow you to specify a starting article and an ending article, and will recursively try to find a series of articles that connect the starting article to the ending article.

This concept in general is based on the idea of [six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation), which theorizes that many people in the world are six or fewer social connections away from any other person in the world. In our context, we are looking to check whether Wikipedia articles for people are six or fewer links away from another.

## Recursive Algorithm

The Wiki crawler will be implemented recursively. From the starting page, the crawler will assemble a list of all of the links to articles found on the page, and will recursively visit those pages to determine if the ending page can be found. Here's another view of what it might look like to try to connect Lupita Nyong'o to Steven Spielberg with a depth limit of 2:

<img
  src="/images/midterm-project-tree-1.svg"
  alt="Diagram showing the connections between articles on Wikipedia."
  style="width:500px;"
/>

Starting from Lupita Nyong'o's page, we found links to articles for Steve McQueen, Chiwetel Ejiofor, and Jordan Peele. We need to recursively search through the connected articles.

First, we recursively visit the article for Steve McQueen. This is not Steven Spielberg, so we need to recursively visit the articles on his page. We next recursively visit the article for Brad Pitt. Again this is not Steven Spielberg, however, this time we do not recursively visit any articles linked from Brad Pitt's page. At this point, we have reached the depth limit (2), and must therefore backtrack to consider other articles linked from Steve McQueen's page.

We similarly visit the page for Viola Davis, which is again not the page we are looking for, and have again reached our depth limit. However, when we go to other articles on Steve McQueen's page, we find that we have exhausted all options for articles, and must therefore backtrack further to consider other direct links on Lupita Nyong'o's page.

From there, we recursively visit Chiwetel Ejiofor's article and then John Cusack's article before again reaching our depth limit. Finally, the next article that we consider is indeed the article for Steven Spielberg -- we have found a connection within the depth limit! Therefore, our recursive calls can return the fact that the connection was found successfully.

However, it's also possible for the crawler to fail to find a connection. For example, given the diagram above, what would happen if we tried to connect Lupita Nyong'o to Tom Cruise? In that case, we would still search each "path" recursively, going up to the depth limit before returning back up to search other articles, but eventually we would exhaust all options and need to return the fact that a connection was not found.

This is the algorithm that you will implement. It is a specific case of the more general Web crawler concept discussed in the lessons.

## Starter Code

You are given two files to start with. It is recommended that you read through the given files to gain an understanding of what is already provided, and what you must implement. Taking the time to read this description and the provided files will make your work on the project much easier!

The files are:

- `wiki_crawler.py`, which is a class that represents the object that will perform the Web crawling. It has a single instance variable, `self.max_depth`, which represents the maximum allowed depth of recursion during crawling. It also contains some functions already written for you:
  - `article()`, which given an article name (e.g., "Philosophy") will fetch the article from the English language Wikipedia (https://en.wikipedia.org/wiki/Philosophy) by issuing an *HTTP request* for the Web page using the Python `requests` library. The function returns the *HTTP response* as a `Response` object. Additional details about this object will be supplied below.
  - `articles_linked_from()`, which given an article name (e.g., "Chiwetel Ejiofor"), will return a list of the Wikipedia articles that are linked from that article. For example, Chiwetel Ejiofor's [Wikipedia article](https://en.wikipedia.org/wiki/Chiwetel_Ejiofor) contains a link to the Wikipedia article for his sister, Zain Asher, as well as director Steven Spielberg. This function will return all such article names: e.g., `articles_linked_from("Chiwetel Ejiofor")` returns `[ "Zain Asher", "Steven Spielberg", ... ]`.
  - `is_name()`, which given a string will return whether that string is likely a person's name. We consider names to be a given name followed by a surname, which both are of the following format: a capital letter A-Z, followed by possibly some number of other letters A-Z, a-z, hyphens ("-"), and apostrophes ("'"). This is a *heuristic* function, meaning it provides a *rule of thumb* that may or may not be correct in all cases. Indeed, this function may mistakenly characterize some non-name string as names, or fail to recognize some names. However, we will use it as a simplifying assumption to try to narrow our search to only articles that represent people.
  - Stub implementations of `connected()` and `crawl()`, which are the two functions that you will write. More details are provided below.

- `test_wiki_crawler.py`, which contains unit tests for `WikiCrawler` objects. Because the `connected()` and `crawl()` methods are not yet implemented, some of the unit tests will fail. As you work on the crawler, you should periodically test it using the current set of unit tests, and also add your own.

## Obtaining Packages

In order to perform the Web crawling, we will need two Python packages:

* `requests` for fetching content over the Web
* `beautifulsoup4` for extracting information from Web pages

To install these packages, enter the following into the VS Code terminal:

```console
python3 -m pip install requests
python3 -m pip install beautifulsoup4
```

## Steps to Complete

### Task 1: Implement `connected()`

Implement the `connected()` method in the `WikiCrawler` class. This method accepts two parameters: a starting article name and an ending article name, and returns whether those two articles can be connected within `self.max_depth` links from each other (either `True` or `False`).

Note that this method is *not* the recursive method. Instead, this method should check whether the given parameters represent actual articles on Wikipedia, and then invoke the recursive `crawl()` method to do the actual crawling.

Here are some additional implementation tips:

- To check whether the `start` and `end` parameters represent valid Wikipedia articles for people, you should use the `article()` function, which returns a [`Response`](https://requests.readthedocs.io/en/latest/api/#requests.Response) object. The `Response` object represents the HTTP request for an article. To determine whether the request for the article was successful, you will need to inspect the `status_code` field of the `Response` object. If the article is not found, the return value will be some value other than `200`.

- If either article is not valid, `connected()` should return `False`.

- The method should then invoke the `crawl()` method to start the recursive Web crawling, beginning the recursion from `start` at a depth of `0`. Note that you must use the return value of the `crawl()` method to determine what `connected()` should ultimately return.

Once you complete this task, the unit tests that evaluate `connected()` for valid start and end pages should be successful. If not, you may need to debug your implementation. Unit tests that check for the success of Web crawling will not yet be successful, since the `crawl()` method is not yet implemented.

### Task 2: Implement `crawl()`

Implement the recursive `crawl()` method to try to connect the starting article with the ending article within `self.max_depth` levels of recursion. Use the `depth` parameter to track which level of recursion the method is currently considering.

- Think about your base cases first. In what cases can the recursion stop? This algorithm should have two base cases: one where the search is successful, and one where it is not (yet) successful because we have exceeded the maximum search depth.

- Implement your recursive logic next. To do so, you will need to recursively visit all of the links that represent people on the current page. To get all of the links to other Wikipedia articles on a given page, you should call the `articles_linked_from()` function.

- Remember to correctly maintain the `depth` parameter as the depth of your recursion increases.

- If a recursive call returns `True`, this means that the search was successful down that recursive path. You do not need to continue searching once you know that the search was successful.

- You can only know that it's not possible to connect the current article to the ending article once you've recursively explored **all** links on the current article.

- The recursive algorithm that you write will be very similar to the Web crawler algorithm discussed in the lessons.

At this point, the remaining unit tests should be testable. Add your own to test whether two people can be connected at various depth limitations.

However, you may notice that some of the unit tests take a long time (minutes) to complete. Can we do better?

### Task 3: Improving your algorithm

At this point, the algorithm does a fairly good job trying to connect articles that represent people on Wikipedia. The `is_name()` heuristic reduces the search space of possible articles to consider, allowing us to search more quickly.

However, we have a problem: we are likely considering some articles *multiple* times. For example, we might have the following connection of articles:

<img
  src="/images/midterm-project-tree-2.svg"
  alt="Diagram showing the connections between articles on Wikipedia, with some articles repeating."
  style="width:500px;"
/>

Indeed, the same article can appear multiple times in the space that we are searching -- leading us to needlessly redo work as we make recursive calls through articles that we have already checked!

Improve the time efficiency of your algorithm by adding a data structure to keep track of which articles have already been visited. Articles that have already been visited do not need to be considered again. Add your data structure as an instance variable of `WikiCrawler` objects. Built-in Python data structures are suitable for this task.

Once complete, try re-running the unit tests as before. You should notice a significant improvement in the amount of time that they take!
