import os.path
import random

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired




#form class, 'search' is the search field. Contents of the user's input are accessed as <formObjectName>.search.data
class MyForm(FlaskForm):
    search = StringField('Enter a query:', validators=[DataRequired()]) 


site = Flask(__name__)


#Code for the search page, generates a form object and then if the user submits a search, redirects to the results page
@site.route('/', methods=('GET','POST'))
def submit():
    form = MyForm()
    if form.is_submitted():
    	return render_template('resultsPage.html', Results=generateStuff(form.search.data))
    return render_template('searchPage.html', form=form)

#Results page code (not really sure what this does but if I change much here it breaks so I'm leaving it as is)
@site.route('/resultsPage', methods=['GET','POST'])
def resultsPage():
    return render_template('resultsPage.html', Results=[])

#Config stuff so the site will run
site.config.update(dict(
    SECRET_KEY="123",
    WTF_CSRF_SECRET_KEY="456"
))

#function to test that the results page can handle having a function call in its argument.
def generateStuff(text):
	stuff=[]
	for i in range(10):
		current = []
		for j in range(3):
			current.append(text)
		stuff.append(current)
	return stuff

if __name__ == '__main__':
	site.run(debug=True)