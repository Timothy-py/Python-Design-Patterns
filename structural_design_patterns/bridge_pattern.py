import abc
import requests as rq


class ResourceContent:
    """
    Define the abstractions's interface.
    Maintain a reference to an object which represents the Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes that fetch content.
    """
    @abc.abstractmethod
    def fetch(self, path):
        pass


class URLFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete implementation.
    """

    def fetch(self, path):
        req = rq.request(method='GET', url=path)
        if req.status_code == 200:
            the_page = req.text
            print(the_page)


class LocalFileFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete implementation.
    """

    def fetch(self, path):
        # path is the file path to a text file
        with open(path) as f:
            print(f.read())


if __name__ == '__main__':
    url_fetcher = URLFetcher()
    interface = ResourceContent(url_fetcher)
    interface.show_content('http://google.com')

    print('=======================================')

    locals_fetcher = LocalFileFetcher()
    interface = ResourceContent(locals_fetcher)
    interface.show_content('../data/movies.json')