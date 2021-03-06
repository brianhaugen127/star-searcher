# Team ExoTerra
# CS483: Web Data
# Final Project
# Scrapes wikipedia for the list of exoplanets
# and builds a database from the information 

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
        result = result.replace("\n", " ")

        try:
            image =  soup.find('meta', property="og:image" ).get("content")
            image = image.replace("\n", "")
            image = image.replace(",", "")


            return (result, image)
        except:
            return (result, " ")
    except:
        print("There is no image and/or remarks")
        return (" " , " ")
    


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
            row.append('imageURL')
            result.append(row)

            for row in reader:
                
                # add new column values
                row.append(formatWikiURL( row[0] ))
                wikiResult = returnWikiText(row[12])
                row.append( wikiResult[0])  #append wikiText
                row.append( wikiResult[1])  #append wiki Image URL
                result.append(row)

                i += 1
                print (i)

                writer.writerows(result)
                result = []



            




if __name__ == '__main__':
    main()
