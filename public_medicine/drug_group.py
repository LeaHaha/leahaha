import csv

npi_p=open("npi_priscribing.csv","rU")
npi_p_csv=csv.reader(npi_p,dialect='excel')
npi_p_list=list(npi_p_csv)


drug=dict()
for index, row in enumerate(npi_p_list):
	print index
	if index !=0:
		if row[0] in drug:
			temp=doctor[row[1]];
			temp[0]=temp[0]+float(row[2])
			temp[1]=temp[1]+float(row[3])
			temp[2]=temp[2]+float(row[4])
			temp[3]=temp[3]+float(row[5])
			temp[4]=temp[4]+float(row[6])
			drug[row[1]]=temp
		else:
			temp=[]
			temp.append(float(row[2]))
			temp.append(float(row[3]))
			temp.append(float(row[4]))
			temp.append(float(row[5]))
			temp.append(float(row[6]))
			drug[row[1]]=temp


res=[]
temp=[]
temp.append("drug")
temp.append('total_claim_count')
temp.append('total_claim_count_daw1')
temp.append('total_quantity_sum')
temp.append('total_day_supply')
temp.append('total_cost_sum')
res.append(temp)
for key,value in drug.iteritems():
	temp=[]
	temp.append(key)
	temp.extend(value)
	res.append(temp)

wfile=open('drug.csv','wb')
writer=csv.writer(wfile)
writer.writerows(res)



