__author__ = "Fenna Feenstra and Martijn AB"

import re


class Html:


    def __init__(self,address):
        """

        :param address:
        """
        print(re.fullmatch(address))
        print(re.fullmatch("onzin"))


class InternetConnection:

    def __init__(self,address):
        """

        :param address:
        """
        run = Html(address)
        # if type(address) == Html: # chek if html

