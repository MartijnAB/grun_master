# #### !/usr/bin/env python3
#
# __author__ = "Fenna Feenstra"
#
# import urllib.request, urllib.parse, urllib.error
# import ssl
# from bs4 import BeautifulSoup
# import re
# import pandas as pd
#
#
# def hack_ssl():
#     """ ignores the certificate errors"""
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
#     print(ctx)
#     return ctx
#
#
# def open_url(url):
#     """ opens url"""
#     ctx = hack_ssl()
#     html = urllib.request.urlopen(url, context=ctx).read()
#     # print(html)
#     return html
#
#
# def fetch_tables(html):
#     """ reads html file as a big string and cleans the html file to make it
#         more readable. input: html, output: tables
#     """
#     soup = BeautifulSoup(html, 'html.parser')
#     # tables = soup.findAll(attrs={'class': re.compile(r".*\bwikitable\b.*")})
#     tables = soup.findAll(attrs={'class': re.compile(r".*\btable\b.*")})
#     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     print(tables)
#     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     return tables[0]
#
#
# def table_df(table):
#     """parses the html table to a pandas dataframe"""
#     # fetch dimensions
#     # print(help(table))
#
#     l = len(table.find_all('tr'))
#     # print(l)
#     # input()
#     w = len(table.find_all('tr')[0].find_all('td'))
#     # print(w)
#     # input()
#     matrix = [['' for i in range(0, w)] for i in range(0, l)]
#     # print(matrix)
#     # input()
#     # fetch content
#     for i, row in enumerate(table.find_all('tr')):
#         print(i)
#         print(row)
#         input()
#         print(row.find_all('td'))
#         for j, column in enumerate(row.find_all('td')):
#             print("b")
#             print(j)
#             print(column)
#             input()
#             print()
#             matrix[i][j] = column.get_text().strip()
#             print(matrix)
#     # put in df making first row the header
#     df = pd.DataFrame(matrix[1:], columns=matrix[0])
#     return df
#     # print(help(table))
#
#     # l = len(table.findall('tr'))
#     # w = len(table.findall('tr')[0].find_all('td'))
#     # matrix = [['' for i in range(0, w)] for i in range(0, l)]
#     # # fetch content
#     # for i, row in enumerate(table.findall('tr')):
#     #     for j, column in enumerate(row.find_all('td')):
#     #         matrix[i][j] = column.get_text().strip()
#     # # put in df making first row the header
#     # df = pd.DataFrame(matrix[1:], columns=matrix[0])
#     # return df
#
#
# def main():
#     # html = open_url('https://en.wikipedia.org/wiki/Tilburg_Trappers')
#     html = open_url('https://www.knmi.nl/nederland-nu/seismologie/aardbevingen')
#     t = fetch_tables(html)
#     df = table_df(t)
#     print(df)
#     print("hallo")
#     # return 0
#
#
# main()
