Exo planet-searcher application

This application uses the wikipedia API to webscrape information
about exo planets. The user can then use a key word search of the
created database.

To run:
1. From CMD line: $python web_scraper.py
   This runs the python webscrapper that scrapes wikipedia
   for exo planet information and builds a .csv names "exo.csv"
   WARNING: This may take some time.

2. At the CMD line: $python flaskserver.py

3. This should return a url to copy/paste into a web browser.
   Use Chrome, Firefox, or Safari. Other browsers were not checked
   for compatibility, but should work.

4. To exit the program, close the browsing window and at the CMD line,
   use 'CTRL-c' to quit the app.