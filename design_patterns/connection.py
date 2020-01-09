#### !/usr/bin/env python3

__author__ = "Fenna Feenstra"

import ssl

def hack_ssl():
    """ ignores the certificate errors"""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def main():
    pass

if __name__ == "__main__":
    main()
