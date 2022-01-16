import pandas
import requests
from bs4 import BeautifulSoup

def webscraper(address):
    html_content = requests.get(address).text
    html_processed = BeautifulSoup(html_content, "lxml")
    return html_processed

def tableprocessor(table_url):
    table = table_url.find("table")
    table_headings = table.find("thead")
    table_body = table.find("tbody")
    clean_table = []

    for row in table_headings.find_all("tr"):
        cols = row.find_all("th")
        cols = [cake.text.strip() for cake in cols]
        clean_table.append(cols)

    for row in table_body.find_all("tr"):
        cols = row.find_all("td")
        cols = [cake.text.strip() for cake in cols]
        clean_table.append(cols) #turn this into functions

    return clean_table

url="https://www.doglost.co.uk/dog-search.php?status=Lost"

dog_html = webscraper(url)

dog_table = tableprocessor(dog_html)

pandas.set_option('display.max_columns', None)

print(pandas.DataFrame(dog_table))
