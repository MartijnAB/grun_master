from Assignment_01.InternetConnection import InternetConnection
# # import InternetConnection
# from Documents.school.Assignment_01.InternetConnection import InternetConnection

__author__ = "Fenna Feenstra and Martijn AB"

# import urllib.request, urllib.parse, urllib.error
# import ssl
# from bs4 import BeautifulSoup
# import re
# import pandas as pd



def main():
    """

    :return: none
    """
    print("exampel1 start")
    run =  InternetConnection('https://en.wikipedia.org/wiki/Tilburg_Trappers')
    print("exampel1 stop")
    print("exampel2 start")
    run = InternetConnection('onzin')
    print("exampel2 stop")


if __name__ == '__main__':
    main()