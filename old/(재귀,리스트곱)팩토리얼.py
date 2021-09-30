# coding=utf-8
#

from selenium import webdriver
from urllib.request import urlopen
import urllib
import pandas as pd
import numpy as np
import json
import sqlite3
import webbrowser
import sys

def factorial(N):
    if N == 0:
        return
    z.append(N)
    N -= 1
    factorial(N)

def list_m(a):
    y = 1
    for i in range(a):
        y *= z[i]
    return print(y)

if __name__ == "__main__":
    N = int(input())
    z = []
    factorial(N)
    a = len(z)
    list_m(a)
