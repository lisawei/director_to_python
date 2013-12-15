import os, sys

import urllib
import json


def read_api(url):
    return urllib.urlopen(url).read()


def read_json(url):
    return json.loads(urllib.urlopen(url).read())


if __name__ == "__main__":
    print read_api("http://api.douban.com/book/subject/1220562?alt=json")
    data = read_json("http://api.douban.com/book/subject/1220562?alt=json")
    print data
    print data["db:tag"]
    print data["title"]

