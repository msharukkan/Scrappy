from bs4 import BeautifulSoup as bs
import urllib2
import json
import inspect, os

targetPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
targetFileName = "Led Traders & wholesalers"
totalData = []

def runAll(count):

    contents = urllib2.urlopen("file:///"+ targetPath + targetFileName + ".html").read()    
    soup = bs(contents, 'html.parser')

    allTitles = soup.findAll('div', attrs = { 'class' : 'r-cl b-gry' })
    totalCount = {}
    totalCount['totalcount'] = len(allTitles)
    totalData.append(totalCount)

    for i in range (0, len(allTitles)):
        
        contact = allTitles[i].find('span', attrs = { 'class' : 'ls_co phn bo' })
        contact = contact.get_text()
        contact = contact.replace('Call ', '')
        name = allTitles[i].find('h4', attrs = { 'class' : 'lcname' })
        address = allTitles[i].find('p', attrs = { 'class' : 'sm clg' })

        data = {}         
        data['contact'] = contact
        data['name'] = name.get_text()
        data['address'] = address.get_text()

        totalData.append(data)

for count in range (1, 2):
    runAll(count)
with open('output/'+ (targetFileName) + '.json', 'w') as outfile:  
    json.dump(totalData, outfile)

print  "-----------------------------------" 
print  "-----------------------------------" 
print "Done"
print " "
print " "
print "Output crated as " + (targetFileName) + ".json"
print " "
print  "-----------------------------------" 
print  "-----------------------------------" 