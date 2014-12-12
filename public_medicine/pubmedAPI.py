from Bio import Entrez
from Bio import Medline
import time
import urllib2
#must enter email
Entrez.email = "ljiang@findthebest.com"
import csv
def main():
    info=open("doctors.csv","rU")
    info_csv=csv.reader(info,dialect='excel')

    wfile=open('list_publication_13_withID.csv','wb')
    writer=csv.writer(wfile)
    for row in info_csv:
        try:
            temp=retrive_record(row)
            writer.writerow(temp)
        except urllib2.URLError:
            time.sleep(300)
            temp=retrive_record(row)
            writer.writerow(temp)


def retrive_record(row):

    name=row[1]+"[AUTH]"        
    handle = Entrez.esearch(db="pubmed",term=name)
    record=Entrez.read(handle)
    idlist=record["IdList"]
    

    
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                       retmode="text")
    records = Medline.parse(handle)

    for record in records:
        temp=[]
        temp.append(row[0])
        temp.append(row[1])
        #title
        temp.append(record.get("TI","?"))
        #authors
        temp.append(record.get("AU","?"))
        #
        temp.append(record.get("AD","?"))
        #
        temp.append(record.get("DP","?"))
        #pubmed id for url
        temp.append(record.get("PMID","?"))

    return temp


if __name__ == '__main__':
    main()
