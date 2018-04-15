 #lucky.py

import requests, sys, webbrowser, bs4
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')

print('Googling...')
# display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug(res)
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")
# Open a browser tab for each result.
linkElems = soup.select('.r a')
logging.debug(linkElems)

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+ linkElems[i].get('href'))
	print (webbrowser)