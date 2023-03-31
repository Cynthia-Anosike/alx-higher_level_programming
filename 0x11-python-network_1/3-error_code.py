#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
Usage: ./3-error_code.py <url>
    -Handles HTTP errors.
"""
import sys
import urllib.request as urll
import urllib.error as err

if __name__ == "__main__":
    url = sys.argv[0]

    request = urll.Request(url)
    try:
        with urll.urlopen(request) as response:
            print(response.reade().decode("ascii"))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
