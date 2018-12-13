# Scrapping Lib
from bs4 import BeautifulSoup as bs
# For Downloading the URI
import urllib2,cookielib
# For CSV
# import csv
# For json
import json, time

totalData = []


def getNumber(str_passed):
        number = ''
        if (str_passed == 'icon-dc'):
                number =  '+'
        if (str_passed == 'icon-fe'):
                number =  ''
        if (str_passed == 'icon-hg'):
                number =  ''
        if (str_passed == 'icon-ba'):
                number =  ' '
        if (str_passed == 'icon-acb'):
                number =  '0'
        if (str_passed == 'icon-yz'):
                number =  '1'
        if (str_passed == 'icon-wx'):
                number =  '2'
        if (str_passed == 'icon-vu'):
                number =  '3'
        if (str_passed == 'icon-ts'):
                number =  '4'
        if (str_passed == 'icon-rq'):
                number =  '5'
        if (str_passed == 'icon-po'):
                number =  '6'
        if (str_passed == 'icon-nm'):
                number =  '7'
        if (str_passed == 'icon-lk'):
                number =  '8'
        if (str_passed == 'icon-ji'):
                number =  '9'
        return number

def runAll(count):
        
        time.sleep(3)
        site= "https://www.justdial.com/Chennai/Home-Delivery-Restaurants/page-" + str(count)
        print "URL Crawled : " + site
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
        
        allTitles = soup.findAll('li', attrs = { 'class' : 'cntanr' })
        for i in range (0, len(allTitles)):
                # For Getting the Price
                data = {} 
                name = allTitles[i].find('span', attrs = { 'class' : 'lng_cont_name' })        
                address = allTitles[i].find('span', attrs = { 'class' : 'cont_fl_addr' })
                contact_info = allTitles[i].find('p', attrs = { 'class' : 'contact-info' })
                new_contact_info = contact_info.find('b')
                if not new_contact_info:
                        new_contact_info = contact_info.find('a')
                
                contactdata = new_contact_info.find_all("span")
                
                total_number = ''
                for cont in contactdata:
                        total_number = total_number + getNumber(cont['class'][1])
                
                data['contact'] = total_number
                data['name'] = name.get_text()
                data['address'] = address.get_text()
                totalData.append(data)


print  "-----------------------------------" 
for i in range (1, 51):
        runAll(i)     
with open('jd.json', 'w') as outfile:  
    json.dump(totalData, outfile)
print  "-----------------------------------" 