# Group 4 
# CS483: Web Data
# Final Project
# Scrapes wikipedia for the list of exoplanets
# and builds a database from the information 

import gzip
import io
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def formatWikiURL( name):
    terms = name.split(' ')
    URL = "https://en.wikipedia.org/wiki/"
    URL = URL + name
    URL = URL.replace(" " , "_")
    URL = URL.replace("+" , "%2B")
    return URL

def returnWikiText(wiki):
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(wiki, headers=header)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        result = soup.find('div',id="bodyContent").text
        result = result.replace(",", " ")
        return result
    except:
        return " "
    


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
    exo.to_csv("exo.csv", mode='w', header = False, index = False, encoding = 'utf-8')

    i = 0
    with open('exo.csv','r') as f_in:
        with open('exoUpdated.csv', 'w') as f_out:
            writer = csv.writer(f_out, delimiter=',', lineterminator='\n')
            reader = csv.reader(f_in, delimiter=',')

            result = []
            # read headers
            row = next(reader)
            # add new header to list of headers
            row.append('URL')
            row.append('wikiText')
            result.append(row)

            writer.writerows(result)
            

            for row in reader:
                result = []
                # add new column values
                row.append(formatWikiURL( row[0] ))
                row.append(returnWikiText(row[12]))
                result.append(row)

                i += 1
                print (i)
                if ( i <= 10):
                    print(row[13])
                if ( i > 100):  #remove this and run again 
                    break       #remove this too


                writer.writerows(result)


            




if __name__ == '__main__':
    main()
