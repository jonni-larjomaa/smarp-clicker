#!/usr/bin/env python

from selenium import webdriver
import time, sys, getopt

def run(url, clicks):
    if url == "":
        raise Exception("no url defined!")
    for cnt in xrange(0,int(clicks)):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.privatebrowsing.autostart", True)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.get(url)
        # just to keep browser open as long as click is counted.
        time.sleep(3)
        browser.quit()


def resolve_opts():
    opts, args = getopt.getopt(sys.argv[1:], "", ["clicks=", "url="])
    clicks = 0
    url = ""
    for opt, value in opts:
        if opt == "--clicks":
            clicks = value
        if opt == "--url":
            url = value
    return url,clicks


if __name__ == '__main__':
    url, clicks = resolve_opts()
    try:
        run(url,clicks)
    except Exception as e:
        print e
        sys.exit(1)
