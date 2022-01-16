import pandas as pd
import mechanicalsoup
import wget
import os

'''scraper = pd.read_html("https://www.doglost.co.uk/dog-search.php?status=Lost")

print(scraper)
'''
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.doglost.co.uk/dog-search.php?status=Lost")
browser.select_form('form[id="dogSearch"]')
browser.form.print_summary()
response = browser.submit_selected()
browser.launch_browser()

