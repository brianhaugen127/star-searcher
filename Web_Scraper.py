# Thomas Dill
# CS483: Web Data
# Assignment 1

import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

def formatWikiURL( name):
    terms = name.split(' ')
    URL = "https://en.wikipedia.org/wiki/"
    URL = URL + name
    URL = URL.replace(" " , "_")
    URL = URL.replace("+" , "%2B")
    return URL


def main():
    # This is the URL to scrape
    URL = "https://en.wikipedia.org/wiki/List_of_exoplanets_(full)"

    # Uses requests to get the URL for the scrape
    r = requests.get(URL)

    # Use BeautifulSoup to get the data in lxml format
    soup = BeautifulSoup(r.content, 'lxml')

    # Retrieve any related tables
    table = soup.findAll('table')

    # Read the HTML format table using pandas
    exo = pd.read_html(str(table) , encoding='utf-8' )[0]


    # Write the data to a CSV file
    exo.to_csv("exo.csv", mode='a', header = False, index = False, encoding = 'utf-8')

    
    with open('exo.csv','r') as f_in:
        with open('exo_plusURl.csv', 'w') as f_out:
            writer = csv.writer(f_out, delimiter=',', lineterminator='\n')
            reader = csv.reader(f_in, delimiter=',')

            result = []
            # read headers
            row = next(reader)
            # add new header to list of headers
            row.append('12')
            row = next(reader)
            row.append('URL')
            result.append(row)

           

            for row in reader:
                # add new column values
                row.append(formatWikiURL( row[0] ))
                result.append(row)

            writer.writerows(result)




if __name__ == '__main__':
    main()