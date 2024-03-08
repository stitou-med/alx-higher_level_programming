#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    req = requests.get(link)
    print(req.headers.get("X-Request-Id"))
