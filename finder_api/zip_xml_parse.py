import urllib2
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import csv

zipcode = open("zip_county_122014.csv", "rU")
zipcode_csv = csv.reader(zipcode, dialect = 'excel')
zipcode_list = list(zipcode_csv)

res = []
for row in zipcode_list:
    print row[0]
    try:
        base = "https://api.finder.healthcare.gov/v3.0/getCountiesForZip"
        row[0] = row[0].zfill(5)
        print row[0]
        zip = row[0]
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <p:ZipCodeValidationRequest xmlns:p="http://hios.cms.org/api" xmlns:p1="http://hios.cms.org/api-types" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://hios.cms.org/api hios-api-11.0.xsd ">
          <p:ZipCode>"""+zip+"""</p:ZipCode>
        </p:ZipCodeValidationRequest>
        """
        
        r = urllib2.Request(base, data = xml, headers = {'Content-Type': 'application/xml'})
        u = urllib2.urlopen(r)
        response = u.read()
        root = ET.fromstring(response)
        temp = []
        for key in root[1][0]:
            temp.append(key.text)
            print temp
        for z in root[2]:
            temp.append(z.text)
        
        res.append(temp)
        
    except urllib2.HTTPError:
        temp = []
        temp.append(row[0])
        temp.append(" ")
        
        res.append(temp)
print res

with open('counties_zip.csv','wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(res)
    
csvfile.close()

