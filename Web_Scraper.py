# Thomas Dill
# CS483: Web Data
# Assignment 1

import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

# This is the URL to scrape
URL = "https://en.wikipedia.org/wiki/List_of_exoplanets_(full)"

# Uses requests to get the URL for the scrape
r = requests.get(URL)

# Use BeautifulSoup to get the data in lxml format
soup = BeautifulSoup(r.content, 'lxml')

# Retrieve any related tables
table = soup.findAll('table')

# Read the HTML format table using pandas
exo = pd.read_html(str(table))[0]


# Write the data to a CSV file
exo.to_csv("exo.csv", mode='a', header = True, index = False)
