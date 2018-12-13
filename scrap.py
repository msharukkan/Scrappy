# Scrapping Lib
from bs4 import BeautifulSoup as bs
# For Downloading the URI
import urllib2
# For CSV
# import csv
# For json
import json

totalData = []

def runAll():

    contents = urllib2.urlopen("https://www.orientelectric.com/contact-us/store-locator").read()
    
    soup = bs(contents, 'html.parser')
    
    allTitles = soup.findAll('div', attrs = { 'class' : 'list' })

    print len(allTitles)
    
    for i in range (0, len(allTitles)):
        
        name = allTitles[i].find('h3')

        contact = allTitles[i].find('p')
        contact = contact.get_text()
        contact = contact.replace('\nPhone: ', ';')
        contact = contact.replace('\r\n\t\t\t\t\t\t\t\t\t\t\t\t', '')
        contact = contact.replace('\n\n', '')

        
        
        data = {} 

        data['name'] = name.get_text()
        data['contact'] = contact

        totalData.append(data)

        # print product_link
        # print product_name
        # print "" 
        # print i


# for count in range (1, 23):
runAll()

with open('output/orientelectric.json', 'w') as outfile:  
    json.dump(totalData, outfile)

# print len(json_data)
print  "-----------------------------------" 
print  "-----------------------------------" 
# print json_data





