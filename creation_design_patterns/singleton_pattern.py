import urllib.parse
import urllib.request


class URLFetcher:
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls


if __name__ == "__main__":
    fetcher = URLFetcher()
    fetcher2 = URLFetcher()
    # fetcher.fetch("https://xkcd.com/353/")
    # print('\n')
    # fetcher2.fetch("https://www.google.com")
    # print(fetcher.urls)
    print(fetcher is fetcher2)


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls

    def dump_url_registry(self):
        return ', '.join(self.urls)


if __name__ == "__main__":
    print(URLFetcher() is URLFetcher())
