"""
This script transforms certain columns of a TSV from Cantus DB based on the
Cantus DB url.
It takes one command line argument, it's the TSV's filename.
"""
import os
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

tsv_filename = os.path.join(os.path.dirname(__file__), sys.argv[1])

def get_html_title(url):
    """
    This function sends a request to the input url and tries to get the title of the 
    HTML page.
    Argument 1: the HTML website that is requested.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.p.string if soup.p else 'No Title Found'
    except requests.RequestException as e:
        return f'Error: {e}'

transforming_column = ['feast','genre','office','source']

df = pd.read_csv(tsv_filename, sep='\t')
df.drop('json_info', axis=1, inplace=True)
for column in transforming_column:
    df[column+'_id'] = f"https://cantusdatabase.org/{column}/" + df[column+'_id'].astype(str)
    df[column+'_name'] = df[column+'_id'].apply(get_html_title)
    print(1)

df.to_csv('cantus_transformed.tsv', sep='\t', index=False)
