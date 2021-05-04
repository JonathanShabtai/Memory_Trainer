import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

major_dictionary = {}

# Parse pages 000 to 999 of https://major-system.info/en/ using beatiful soup and urllib.request
for i in range(0, 1000):
    print(i)  # to keep track of the progress
    if len(str(i)) == 1:  # add 00 before {i}
        source = urllib.request.urlopen(f'https://major-system.info/en/?n=00{i}').read()
    elif len(str(i)) == 2:  # add 0 before {i}
        source = urllib.request.urlopen(f'https://major-system.info/en/?n=0{i}').read()
    else:  # Just use {i}, as we deal with 3 digit numbers to begin with
        source = urllib.request.urlopen(f'https://major-system.info/en/?n={i}').read()
    soup = BeautifulSoup(source, 'lxml')
    body = soup.body

    # Parse the relevant text according to a tag
    for paragraph in body.find_all('div', {'id': 'response'}):
        list_of_words = paragraph.text.split()
        major_dictionary[i] = list_of_words

# Save the table into a .csv file
df = pd.DataFrame.from_dict(major_dictionary, orient='index')
df.to_csv('major_dictionary_original.csv')

df = pd.read_csv('major_dictionary_original.csv', index_col=0)
