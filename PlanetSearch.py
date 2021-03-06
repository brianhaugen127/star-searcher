# This is the Planet Searcher python code that builds
# the schema, and indexes the data using Whoosh.
# Basiaclly, this builds the database and back end
# of the project.


# Importing libraries and whoosh into the project
import csv
import sys
from builtins import input
csv.field_size_limit(sys.maxsize)
import whoosh
import os.path

from os import path
from whoosh import index
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser

# This is a function that is used at the CMD line
# to add in trouble shooting and seting up the
# database.
def search(indexer, searchTerm):
    with indexer.searcher() as searcher:
        query = MultifieldParser(
            ['Remarks', 'wikiText' ], schema=indexer.schema)
        query = query.parse(searchTerm)
        results = searcher.search(query, limit=20)
        print("Length of results: " + str(len(results)))
        for line in results:
            print(line['Name'], line['URL'], line['Distance'] , line['Remarks'], line['imageURL'])
            print (line)

  # This is setting up the database by creating a list of results
        rname = list()
        rUrl = list()
        rDist = list()
        rRem = list()
        rImage = list()
        
        for x in results:
            rname.append(x['Name'])
            rUrl.append(x['URL'])
            rDist.append(x['Distance'])
            rRem.append(x['Remarks'])

# This is the stock image we use if an exoplanet does not have an image.
            if x['imageURL'] == ' ':
                rImage.append("https://assets3.thrillist.com/v1/image/2778565/size/sk-2017_04_article_main_mobile.jpg")
            else:
                rImage.append(x['imageURL'])
        return rname, rUrl, rDist, rRem, rImage

# The following functions return 0 to the database for error checks
def myfloat(number):
    try:
        if u"\u00B1" in number:
            list1 = number.split()
            number = list1[0]
        result = float(number)
        return result
    except:
        return "0"

def myInt(number):
    try:
        result = int(number)
        return result
    except:
        return "0"

# This creates the search index for Whoosh
def index():
    
    #if directory doesn't exist, create myIndex
    if not os.path.exists("myIndex"):
        os.mkdir("myIndex")

    # Create the schema, indexer, and the writer 
    schema = Schema(Name=TEXT(stored=True), Mass=NUMERIC(float, stored=True), Radius=NUMERIC(float, stored=True), Period=NUMERIC(float, stored=True),
        Semi_major_axis=NUMERIC(float, stored=True), Temperature=NUMERIC(stored=True), Discovery_Method=TEXT(stored=True), Discovery_Year=NUMERIC(stored=True),
        Distance=NUMERIC(float, stored=True), hostStarMass=NUMERIC(float, stored=True), hostStarTemp=NUMERIC(float, stored=True) , Remarks=TEXT(stored=True), URL=TEXT(stored=True) , wikiText=TEXT(stored=True), imageURL=TEXT(stored=True))
    
    usages_exists = whoosh.index.exists_in("myIndex", indexname="planetIndex")
    if (usages_exists):
        print("Index already Exists")
        return whoosh.index.open_dir("myIndex", indexname="planetIndex", readonly=False)


    indexer = create_in('myIndex', schema , indexname="planetIndex")
    writer = indexer.writer()

    # open the exoplanet csv file from the web scraper. Note: Must be in the same directory!
    csvfile = open('exoUpdated.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0

    # Read each row of the CSV file and write into myIndex Whoosh index
    for row in reader:
        line_count += 1
        if (line_count == 1):
            continue
        writer.add_document(Name=row[0],
        Mass=myfloat(row[1]), 
        Radius=myfloat(row[2]),
        Period=myfloat(row[3]), 
        Semi_major_axis=myfloat(row[4]), 
        Temperature=myInt(row[5]) , 
        Discovery_Method=row[6],
        Discovery_Year=myInt(row[7]), 
        Distance=myfloat(row[8]), 
        hostStarMass=myfloat(row[9]), 
        hostStarTemp=myfloat(row[10]), 
        Remarks=row[11], 
        URL=row[12],
        wikiText=row[13],
        imageURL=row[14])
        

    print("Total Tuples:",   line_count)
    writer.commit()
    return indexer

# The following commented code was used prior to the Flask server
# being implemented. It allowed the app to run at the cmd line
# and was used for trouble shooting. Feel free to uncomment the code
# to run the application at the cmd line. In this case, you will still
# need to run Web_Scraper.py first to create the data to pull from,
# then type $ python PlanetSearch.py. When finished, simply type exit.

# def main():
    # indexer = index()
    # print('Search for planets')
    # while (True):
    #    print('\n')
    #    print('To exit the program, just type "exit". \n')
    #
    #    searchTerm = input('Please enter a query: ')
    #    if searchTerm == 'exit':
    #        break
    #
    #    results = search(indexer, searchTerm)

    #
    # if __name__ == '__main__':
    #     main()
