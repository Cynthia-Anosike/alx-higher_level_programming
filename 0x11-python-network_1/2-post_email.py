#!/usr/bin/python3
"""A python script that takes in a URL and email, sends a POST request to the
passed URL with the email as a parameter and displays the body of the response
"""
import sys
import urllib.request as urll
import urllib.parse as parsy

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = parsy.urlencode(value).encode("ascii")

    req = urll.Request(url, data)
    with urll.urlopen(req) as response:
    print(response.read().decode("utf-8"))
