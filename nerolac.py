# Scrapping Lib
from bs4 import BeautifulSoup as bs
# For Downloading the URI
import urllib2,time,sys
# For CSV
# import csv
# For json
import json

totalData = []
start = time.time()

def runAll(count):
    if (count == 0):
        count =  1
    time.sleep(20)

    site= "https://nerolac.com/dealer-locator/getstores/P" + str(count)
    
    output_str =  "\nURL Crawled : " + str(site)
    sys.stdout.write(output_str)  
    sys.stdout.flush()

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
    req = urllib2.Request(site, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    contents = page.read()

    soup = bs(contents, 'html.parser')
    allTitles = soup.findAll('div', attrs = { 'class' : 'storeLocatorContainer' })

    for i in range (0, len(allTitles)):
       
        name = allTitles[i].find('h3')
        address = allTitles[i].find('p')
        contact = allTitles[i].find('a')

        data = {} 

        data['name'] = name.get_text()
        data['address'] = address.get_text()
        data['contact'] = contact.get_text()

        totalData.append(data)


sys.stdout.write("ExecutionStarted\n" + str(start))  # same as print
sys.stdout.write("\n-----------------------------------")  # same as print
sys.stdout.flush()

for count in range (0, 2131, 15):
        runAll(count)
with open('nerolacnew.json', 'w') as outfile:  
    json.dump(totalData, outfile)

print  "\n-----------------------------------" 
end = time.time()
print(end - start)