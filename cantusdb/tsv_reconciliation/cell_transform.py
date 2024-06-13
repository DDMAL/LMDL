import requests
import os
import sys
import csv
from bs4 import BeautifulSoup

tsv_filename = os.path.join(os.path.dirname(__file__), sys.argv[1])

def get_html_title(url):
    # Send a request to the URL
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the title tag
    title = soup.title.string
    return title

transforming_column = ['feast_id','genre_id','office_id','source_id']

with open(tsv_filename) as fd:
    tsv_reader = csv.reader(fd, delimiter='\t', quotechar='"')
    for row in tsv_reader:
        
