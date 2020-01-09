import abc
import urllib.parse
import urllib.request
import sys
import connection as con

#define resource content abstraction
class ResourceContent:
    """
    Abstraction interface
    with a reference to an object which
    represents the Implementor
    via attribute _imp
    """
    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)

#define the abstract interface
class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """ interface for implementation classes that fetches content"""
    @abc.abstractmethod
    def fetch(path):
        pass


#implementation of interface
class URLfetcher(ResourceContentFetcher):
    """
    implementation of interface with concrete implementation
    for url fetcher
    """
    def fetch(self, path):
        url = urllib.request.Request(path)
        with urllib.request.urlopen(url, context=con.hack_ssl()) as response:
            if response.code == 200:
                print(response.read())


#implementation of interface
class LocalFileFetcher(ResourceContentFetcher):
    """
    implementation of interface with concrete implementation
    for local file fetcher
    """
    def fetch(self, path):
        with open(path) as f:
            print(f.read())


def main():
    """
    composes an interface to fetch content of location and shows the content
    by creating an instance of an interface implementation and
    assign the abstract interface to that specific interface implementation
    two examples shown
    """
    url_fetcher = URLfetcher() #initiate url_fetcher instance
    iface = ResourceContent(url_fetcher) # assign abstract interface to url_fetcher
    iface.show_content('https://bioinf.nl/~fennaf/poem.txt')

    input("press any key")

    file_fetcher = LocalFileFetcher()
    iface = ResourceContent(file_fetcher)
    iface.show_content('data/KNMI_20181231.txt.tsv')


if __name__ == "__main__":
    exitcode = main()
    sys.exit(exitcode)
