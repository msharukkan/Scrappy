# Scrapping Lib
from bs4 import BeautifulSoup as bs
# For Downloading the URI
import urllib2
# For CSV
# import csv
# For json
import json

totalData = []

def runAll(count):

    contents = urllib2.urlopen("https://www.ramrajcotton.in/men?page=" + str(count)).read()
    
    soup = bs(contents, 'html.parser')
    
    allTitles = soup.findAll('div', attrs = { 'class' : 'product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12' })

    # print len(allTitles)
    
    for i in range (0, len(allTitles)):
        # For Getting the Price
        price = allTitles[i].find('p', attrs = { 'class' : 'price' })
        # print price.get_text()

        # For getting the Product Link and the Name 
        product_list = allTitles[i].findAll('div', attrs = { 'class' : 'prodDet' })[0]
        product_list = product_list.findAll('h4')[0]
        product_link = product_list.find_all('a', href=True)
        product_link = product_link[0]['href']
        product_name = product_list.get_text()

        data = {} 

        data['name'] = product_list.get_text()
        data['price'] = price.get_text()

        totalData.append(data)

        # print product_link
        # print product_name
        # print "" 
        # print i


for count in range (1, 23):
    runAll(count)

json_data = json.dumps(totalData)
print len(json_data)
print  "-----------------------------------" 
print  "-----------------------------------" 
print json_data





