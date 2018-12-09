Exo planet-searcher application

This application uses the Wikipedia API to webscrape information
about exoplanets. The user can then use a key word search of the
created database.

To run:
1. From CMD line:

    $ python Web_Scraper.py

   This runs the python webscrapper that scrapes wikipedia
   for exo planet information and builds a .csv nameed "exo.csv"
   WARNING: This may take some time.

2. If this is the first time running this application, after running
   web_scraper.py, you must run PlanetSearch.py at the cmd line.

    $ python PlanetSearch.py

   This builds the database and index for flask. You only need to run
   PlanetSearch once, or anytime after you run Web_Scraper.py.

3. At the CMD line:

    $ python flaskserver.py

4. This should return a url to copy/paste into a web browser.
   Use Chrome, Firefox, or Safari. Other browsers were not checked
   for compatibility, but should work. The app is best viewed in
   Safari.

5. To exit the program, close the browsing window and at the CMD line,
   use 'CTRL-c' to quit the app.