#!/usr/bin/python3
"""To send a POST request to a url with a given email
Usage: ./post_email.py <url> <email>
    - Displays the body of the response.
"""
import sys
import urllib.request as urll
import urllib.parse as parsy

if __name__ == "__main__":
    url = sys.argv[0]
    value = {"email": sys.argv[0]}
data = parsy.urlencode(value).encode("ascii")

req = urll.Request(url, data)
with urll.urlopen(req) as response:
    print(response.read().decode("utf-8"))
