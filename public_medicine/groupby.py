import csv
npi_p=open("doctor_moreinfo.csv","rU")
npi_p_csv=csv.reader(npi_p,dialect='excel')
npi_p_list=list(npi_p_csv)


#group by state and specialty 
state_specialty=dict()
for index, row in enumerate(npi_p_list):
	if index !=0:
		if row[9] in state_specialty:
			temp=state_specialty[row[9]]
			temp[0]=temp[0]+float(row[1])
			temp[1]=temp[1]+float(row[2])
			temp[2]=temp[2]+float(row[3])
			temp[3]=temp[3]+float(row[4])
			temp[4]=temp[4]+float(row[5])
			state_specialty[row[9]]=temp
		else:
			temp=[]
			temp.append(float(row[1]))
			temp.append(float(row[2]))
			temp.append(float(row[3]))
			temp.append(float(row[4]))
			temp.append(float(row[5]))
			state_specialty[row[9]]=temp


#group by state and specialty 
county_specialty=dict()
for index, row in enumerate(npi_p_list):
	if index !=0:
		if row[10] in county_specialty:
			temp=county_specialty[row[10]]
			temp[0]=temp[0]+float(row[1])
			temp[1]=temp[1]+float(row[2])
			temp[2]=temp[2]+float(row[3])
			temp[3]=temp[3]+float(row[4])
			temp[4]=temp[4]+float(row[5])
			county_specialty[row[10]]=temp
		else:
			temp=[]
			temp.append(float(row[1]))
			temp.append(float(row[2]))
			temp.append(float(row[3]))
			temp.append(float(row[4]))
			temp.append(float(row[5]))
			county_specialty[row[10]]=temp


res_state=[]
temp=[]
temp.append("state_specialty")
temp.append('total_claim_count')
temp.append('total_claim_count_daw1')
temp.append('total_quantity_sum')
temp.append('total_day_supply')
temp.append('total_cost_sum')
res_state.append(temp)
for key,value in state_specialty.iteritems():
	temp=[]
	temp.append(key)
	temp.extend(value)
	res_state.append(temp)



res_county=[]
temp=[]
temp.append("county_specialty")
temp.append('total_claim_count')
temp.append('total_claim_count_daw1')
temp.append('total_quantity_sum')
temp.append('total_day_supply')
temp.append('total_cost_sum')
res_county.append(temp)
for key,value in county_specialty.iteritems():
	temp=[]
	temp.append(key)
	temp.extend(value)
	res_county.append(temp)

wfile=open('state_specialty.csv','wb')
writer=csv.writer(wfile)
writer.writerows(res_state)



wfile=open('county_specialty.csv','wb')
writer=csv.writer(wfile)
writer.writerows(res_county)

