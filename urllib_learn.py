import os, sys

import urllib
import json


if __name__ == '__main__':
    url = 'http://163.com'
    fd = urllib.urlopen(url)
    #print fd.read()

    url2 = "http://api.douban.com/book/subject/1220562?alt=json"
    fs=urllib.urlopen(url2)
    data = fs.read()
    print type(data)

    d=json.loads(data)
    print d
    print type (d)

    print d['title']
    print d['author']
    print d['db:tag']

    for i in d['db:tag']:
        print i['@count'],i['@name']
#
#def read_api(url):
#    return urllib.urlopen(url).read()
#
#
#def read_json(url):
#    return json.loads(urllib.urlopen(url).read())
#
#
#if __name__ == "__main__":
#    print read_api("http://api.douban.com/book/subject/1220562?alt=json")
#    data = read_json("http://api.douban.com/book/subject/1220562?alt=json")
#    print data
#    print data["db:tag"]
#    print data["title"]

