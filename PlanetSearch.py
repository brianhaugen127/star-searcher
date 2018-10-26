import csv
import sys
from builtins import input
csv.field_size_limit(sys.maxsize)
import whoosh

import csv
import sys
from builtins import input

import whoosh
from whoosh import index
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser


def search(indexer, searchTerm):
    with indexer.searcher() as searcher:
        query = MultifieldParser(
            ['Remarks', 'wikiText'], schema=indexer.schema)
        query = query.parse(searchTerm)
        results = searcher.search(query, limit=None)
        print("Length of results: " + str(len(results)))
        for line in results:
            print(line['Name'], line['URL'], line['Distance'])
            #print (line)

def myfloat(number):
    try:
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

def index():
    schema = Schema(Name=TEXT(stored=True), Mass=NUMERIC(float, stored=True), Radius=NUMERIC(float, stored=True), Period=NUMERIC(float, stored=True),
        Semi_major_axis=NUMERIC(float, stored=True), Temperature=NUMERIC(stored=True), Discovery_Method=TEXT(stored=True), Discovery_Year=NUMERIC(stored=True),
        Distance=NUMERIC(float, stored=True), hostStarMass=NUMERIC(float, stored=True), hostStarTemp=NUMERIC(float, stored=True) , Remarks=TEXT(stored=True), URL=TEXT(stored=True) , wikiText=TEXT(stored=True) )
    
    usages_exists = whoosh.index.exists_in("indexdir", indexname="planetIndex")
    if (usages_exists):
        print("Index already Exists")
        return

    indexer = create_in('myIndex', schema , indexname="planetIndex")
    writer = indexer.writer()

    csvfile = open('exoUpdated.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
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
        wikiText=row[13]  )
        

    print("Total Tuples:",   line_count)
    writer.commit()
    return indexer


def main():
    indexer = index()
    print('Search for planets')
    while (True):
        print('\n')
        searchTerm = input('Please enter a query: ')
        if searchTerm == 'exit':
            break
        
        results = search(indexer, searchTerm)


if __name__ == '__main__':
    main()
