__author__ = "Fenna Feenstra and Martijn AB"



import re
from abc import ABC, abstractmethod
import urllib.request, urllib.parse, urllib.error


class HyperTextMarkupLanguage(ABC):

    @abstractmethod
    def __init__(self, address):
        print("wouw dtevvvvvvvvvvvvvvvvvvvvvvvvvvvyyyyyyyyyyyyyyyrrrrrrrrrrrf")

    @abstractmethod
    def is_valied(self):
        pass




class Html(HyperTextMarkupLanguage):


    def __init__(self,address):
        """
        bron reg: https://www.geeksforgeeks.org/python-check-url-string/
        :param address:
        """


        self.is_true_html = False
        if re.fullmatch('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', address):
            self.is_true_html = True
        else:
            import warnings
            warnings.warn("is not a valit html")
            self.__class__ = FalseHtml

    def is_valied(self):
        pass

    # def hack_ssl():

    # """ ignores the certificate errors"""
    #     ctx = ssl.create_default_context()
    #     ctx.check_hostname = False
    #     ctx.verify_mode = ssl.CERT_NONE
    #     print(ctx)
    #     return ctx

    # @


class FalseHtml(HyperTextMarkupLanguage):

    def is_valied(self):
        pass


class InternetConnection:

    def __init__(self,address):
        """

        :param address:
        """
        run = Html(address)

        if isinstance(run, Html):
            print("ja a")
        else:
            print("nee a")

        # if type(address) == Html: # chek if html

    def open_url(url):
        """ opens url"""
        ctx = hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        # print(html)
        return html

