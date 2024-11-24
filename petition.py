#!/bin/python3

import time
import urllib.request, json 
import locale
locale.setlocale(locale.LC_ALL, '')


data = ""
count = 0
newcount = 0

while True:

    with urllib.request.urlopen("https://petition.parliament.uk/petitions/700143.json") as url:
        data = json.load(url)


    #print(data['data']['attributes']['signature_count'])

    time.sleep(5)

    newcount = int(data['data']['attributes']['signature_count'])
    newcount2 = f'{newcount:,}'


    if (newcount > count):
        newsigs = newcount - count
        newsigs2 = f'{newsigs:,}'
        print("There are {0} more signatures!\nTotal is now {1}\n".format(newsigs2, newcount2))
    #    print(newcount)
        count = newcount


