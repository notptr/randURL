#!/usr/bin/env python

#This is free and unencumbered software released into the public domain.

#Anyone is free to copy, modify, publish, use, compile, sell, or
#distribute this software, either in source code form or as a compiled
#binary, for any purpose, commercial or non-commercial, and by any
#means.

#In jurisdictions that recognize copyright laws, the author or authors
#of this software dedicate any and all copyright interest in the
#software to the public domain. We make this dedication for the benefit
#of the public at large and to the detriment of our heirs and
#successors. We intend this dedication to be an overt act of
#relinquishment in perpetuity of all present and future rights to this
#software under copyright law.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <http://unlicense.org/>







#This is a python program that will open up a random url from a list
#It was a weird project for me to come up with
#Devloper: Matthew Deig
#Date: 2014-11-03

import webbrowser, random
from optparse import OptionParser

def argParser():
    #this will return 2 objects
    #the options and args
    parser = OptionParser()
    parser.add_option("-a", "--add", dest="newurl", help="Adds a new url to the list", metavar="NEWURL")
    parser.add_option("-q", "--nobrowser", action="store_true", dest="nobrowser", help="Does not open a broswer just prints the url out")
    return parser.parse_args()

def openBroswer(url):
    webbrowser.open_new_tab(url)

def addUrl(url):
    file = open("url.db", "a")
    file.write(url+"\n")
    file.close()

def readUrls():
    file = open("url.db", "r")
    urls = file.readlines()
    file.close()
    print(urls)
    return urls

def pickUrl(urls):
    #this is probley not very random but it is going to work
    return random.choice(urls)

if __name__ == "__main__":
    (options, args) = argParser()
    
    
    if options.newurl is not None:
        addUrl(options.newurl)
    else:
        if(options.nobrowser):
            print(pickUrl(readUrls()))
        else:
            openBroswer(pickUrl(readUrls()))
