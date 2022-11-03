import csv
import re
import time
from selenium_core import SeleniumBrowser
import openpyxl



def save_file(data):
    with open('mycsvfile.csv', 'w') as f:
        print(data)
        w = csv.DictWriter(f, fieldnames=['name', 'description'])
        w.writeheader()
        w.writerows(data)

wookbook = openpyxl.load_workbook("1000артикулов.xlsx")
products = []
worksheet = wookbook.active

for i in worksheet['A']:

    url_1 = f"https://partscatalog.deere.com/jdrc/partdetails/partnum/{i.value}/"
    page = SeleniumBrowser(url=url_1)
    page.activate()
    page.open_page(url_1)
    time.sleep(3)
    source = page.get_page_source()
    name = source.find('span',  {"class": "partname ng-star-inserted"})
    description = source.find(text=re.compile('Описание')).findNext('div').contents[0]
    product = {"name": name.get_text(), "description": description.get_text()}

    products.append(product)
    page.quit()

save_file(products)


