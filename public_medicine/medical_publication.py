import pandas as pd
import numpy as np
import re
from pandas import *
from numpy import *

#Read publication list api data
l1 = pd.read_csv("list_publication_1_withID.csv")
l2 = pd.read_csv("list_publication_2_withID.csv")
l3 = pd.read_csv("list_publication_3_withID.csv")
l4 = pd.read_csv("list_publication_4_withID.csv")
l5 = pd.read_csv("list_publication_5_withID.csv")
l9 = pd.read_csv("list_publication_9_withID.csv", header = None)
l10 = pd.read_csv("list_publication_10_withID.csv", header = None)
l11 = pd.read_csv("list_publication_11_withID.csv", header = None)
l12 = pd.read_csv("list_publication_12_withID.csv", header = None)
l13 = pd.read_csv("list_publication_13_withID.csv")
l14 = pd.read_csv("list_publication_14_withID.csv")
#unify column names
l1.columns = l13.columns
l2.columns = l13.columns
l3.columns = l13.columns
l4.columns = l13.columns
l5.columns = l13.columns
l9.columns = l13.columns
l10.columns = l13.columns
l11.columns = l13.columns
l12.columns = l13.columns
#Make as one table
c1 = l1.append(l2)
c2 = c1.append(l3)
c3 = c2.append(l4)
c4 = c3.append(l5)
c5 = c4.append(l9)
c6 = c5.append(l10)
c7 = c6.append(l11)
c8 = c7.append(l12)
c9 = c8.append(l13)
c0 = c9.append(l14)
c0.columns = ['id','author','paper_title','co_author','department','date','pmid'] #modify column names
c0.dtypes #chemedpub column data types

#replace ? as NaN
medpub = c0.replace('?',np.nan) 
#Switch data type in two columns for string operations
medpub['department'] = medpub['department'].astype('str')
medpub['co_author'] = medpub['co_author'].astype('str')
#Remove unnecessary symbols and spaces
medpub['department'] = medpub['department'].map(lambda x: x.replace('Calif.','CA'))
medpub['department'] = medpub['department'].map(lambda x: x.replace(' USA','USA'))
medpub['co_author'] = medpub['co_author'].map(lambda x: x.replace('[',''))
medpub['co_author'] = medpub['co_author'].map(lambda x: x.replace(']',''))
medpub['co_author'] = medpub['co_author'].map(lambda x: x.replace("'",''))
#Get first 10 co-author names
medpub['coau'] = medpub['co_author'].map(lambda x: x.split(',',10)[0:10])
medpub['coau'] = medpub['coau'].astype('str')
medpub['coau'] = medpub['coau'].map(lambda x: x.replace('[',''))
medpub['coau'] = medpub['coau'].map(lambda x: x.replace(']',''))
medpub['coau'] = medpub['coau'].map(lambda x: x.replace("'",''))
#Get first 3 items as author's department info, delimiter is ','
medpub['dprt'] = medpub['department'].map(lambda x: x.split(',')[0:3])
medpub['dprt'] = medpub['dprt'].astype(str)
medpub['dprt'] = medpub['dprt'].map(lambda x: x.split(';')[0]) #remove appended info after ';'
#Remove unnecessary symbols and spaces
medpub['dprt'] = medpub['dprt'].astype(str)
medpub['dprt'] = medpub['dprt'].map(lambda x: x.replace('[',''))
medpub['dprt'] = medpub['dprt'].map(lambda x: x.replace(']',''))
medpub['dprt'] = medpub['dprt'].map(lambda x: x.replace("'",''))
medpub['dprt'] = medpub['dprt'].map(lambda x: x.replace('1 ',''))
medpub['dprt'] = medpub['dprt'].map(lambda x: x.replace('1',''))

#Set values as empty string in the department column when including symbols in mylist
mylist = ['@','0','1','2','3','4','5','6','7','8','9']
pattern = '|'.join(mylist)

medpub['dprt'][medpub.dprt.str.contains(pattern) == True] = ''
medpub.dprt.str.contains(pattern).value_counts() #chemedpub if all get repalced

#Department info which will be used for extracting location info
medpub['dprt_temp'] = medpub['department'].map(lambda x: x.split(',')[0:5])
medpub['dprt_temp'] = medpub['dprt_temp'].astype(str)
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.split(';')[0])
medpub['dprt_temp'] = medpub['dprt_temp'].astype(str)

medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('[',''))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(']',''))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("'",''))

#Get ready for applying delimeter "."
medpub['dprt_temp'] = medpub['dprt_temp'].astype(str)
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('S. Adair','S Adair'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('2 Department','.2 Department'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("2University",'.2University'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('M. Everett','M Everett'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('Pathology.','Pathology,'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("F. Perutz",'F Perutz'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(' and.','.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("dagger",'.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" (Dr Lewis),", '.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('UA-SPH','UA-SPH.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(">Medicine",'.Medicine'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" (Dr Lewis),", '.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('Dr.','Dr'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("St.",'St'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Kathryn E.", 'Kathryn E'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Ophthalmology.", 'Ophthalmology'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('67 President Street','.67 President Street'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Institute of MGH",'Institute of MGH.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Andrea M. Sisko ", 'Andrea M Sisko '))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Robert J. Rosati", 'Robert J Rosati'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Taiwan and", 'Taiwan.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('InstituteDr','Institute. Dr'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("University/Chicago",'University. Chicago'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Medical Research Center itoma@gwu.edu", 'Medical Research Center. itoma@gwu.edu'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Drs S. W. Harris", 'Drs S W Harris'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Kansas City tsrivastava@cmh.edu", 'Kansas City. tsrivastava@cmh.edu'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(' Biosciences and p.vajjhala@uq.edu.au.',' Biosciences. and p.vajjhala@uq.edu.au.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("N.Y.",'NY.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("MD Department ", 'MD. Department '))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Laurent G. Glance", 'Laurent G Glance'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Research Center ues3@cornell.edu.",'Research Center ues3@cornell.edu.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('Christopher B. Forrest','Christopher B Forrest'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" Ontario leighanne.",' Ontario. leighanne.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" Initiatives and Melissa Begg ", ' Initiatives. and Melissa Begg '))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("R. Sansone", 'R Sansone'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Research Center itoma@gwu.edu.",'Research Center. itoma@gwu.edu.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(' Medicina 2. Hospital',' Medicina. 2. Hospital'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Iowa drew.d.lewis",'Iowa. drew.d.lewis'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" Research (C.E.N.T.E.R.)", ' Research (CENTER)'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Spain sandraba", 'Spain. sandraba'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("Margaret E. Kruk ",'Margaret E Kruk '))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('Arbor,  MI Division','Arbor, MI. Division'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("(Pa.)",''))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("School of Public Health. Wanna Medical College. Wuhu 241002. China.", 'School of Public Health, Wanna Medical College, Wuhu 241002, China.'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('"',''))

#Split by "."
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.split('.')[0])

#Fixing Data
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("1Assistant Professor", 'Assistant Professor'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("MI 48084 2Assisant", 'MI 48084. 2Assisant'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(" NY Mount Sinai Liver",' NY. Mount Sinai Liver'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace(' IL University of Illinois',' IL. University of Illinois'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("TX Department",'TX. Department'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("CaliforniaDrs",'California. Drs'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace('West China The Chinese','West China. The Chinese'))
medpub['dprt_temp'] = medpub['dprt_temp'].map(lambda x: x.replace("CA Department of Pediatrics ",'CA. Department of Pediatrics '))

#Get the 4-6th Items as Department
medpub['location'] = medpub['dprt_temp'].map(lambda x: x.split(',')[3:5])
medpub['location'] = medpub['location'].astype(str)
medpub['location'] = medpub['location'].map(lambda x: x.split(';')[0])

medpub['location'] = medpub['location'].astype(str)
medpub['location'] = medpub['location'].map(lambda x: x.replace('[',''))
medpub['location'] = medpub['location'].map(lambda x: x.replace(']',''))
medpub['location'] = medpub['location'].map(lambda x: x.replace("'",''))
medpub['location'] = medpub['location'].map(lambda x: x.replace(",",', '))

medpub['location'] = medpub['location'].map(lambda x: x.split('.')[0])
medpub['location'] = medpub['location'].astype(str)
medpub['location'] = medpub['location'].map(lambda x: x.split(',')[0:1])
medpub['location'] = medpub['location'].astype(str)
medpub['location'] = medpub['location'].map(lambda x: x.lstrip())

#remove zipcode attached with state names
medpub['location'] = medpub['location'].astype(str)
medpub['location'] = medpub['location'].map(lambda x: re.sub(r"[^A-z]+", "", x))
medpub['location'] = medpub['location'].map(lambda x: x.replace('[',''))
medpub['location'] = medpub['location'].map(lambda x: x.replace(']',''))
medpub['location'] = medpub['location'].map(lambda x: x.replace("'",''))

#Selecting output columns and rename them
result = medpub[['id','author','paper_title','coau','date','pmid','dprt','location']]
result.columns = ['id', 'author', 'paper_title', 'co_author', 'date', 'pmid', 'department', 'location']
#File output
result.to_csv('medpublist.csv')
