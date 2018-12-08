
from flask import Flask, render_template, url_for, request
import whoosh
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
from whoosh import qparser
from PlanetSearch import search
from PlanetSearch import index

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def myindex():
	print('HEya')
	return render_template('welcome_page.html')

@app.route('/my-link/')
def my_link():
	print('clicked')
	return 'Click'

@app.route('/results/', methods=['GET', 'POST'])
def results():
	global mysearch
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args

	keywordquery = data.get('searchterm')
	#test = data.get('test')

	print('Keyword Query is: ' + keywordquery)
	#print('Test Query is: ' + test)

    #Get the results from the search in whooshtest.py 
	name, url, dist, remarks, imageURL = search(index(), keywordquery)
	print(remarks)
    
    #Render the results to myresults
	return render_template('results.html', query=keywordquery, results=zip(name, url, dist, remarks, imageURL))


if __name__ == '__main__':
	global mysearch
	app.run(debug=True)
