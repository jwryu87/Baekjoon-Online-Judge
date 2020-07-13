# coding=utf-8
#

from selenium import webdriver
from urllib.request import urlopen
import urllib
import pandas as pd
import json
import sqlite3
import webbrowser
import sys

x, y, w, h = map(int, input().split())
z = []
z.append(x)
z.append(w-x)
z.append(y)
z.append(h-y)
print(min(z))


# if __name__ == "__main__":
    