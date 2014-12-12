
import csv
npi_p=open("doctor.csv","rU")
npi_p_csv=csv.reader(npi_p,dialect='excel')
npi_p_list=list(npi_p_csv)

doctor=dict()
for index, row in enumerate(npi_p_list):
	if index !=0:
		doctor[row[0]]=row[1:]


app_doctor=open("app_doctors.csv","rU")
app_doctor_csv=csv.reader(app_doctor,dialect='excel')
app_doctor_list=list(app_doctor_csv)

res=[]
temp=[]
temp.append("npi")
temp.append('total_claim_count')
temp.append('total_claim_count_daw1')
temp.append('total_quantity_sum')
temp.append('total_day_supply')
temp.append('total_cost_sum')
temp.append('state')
temp.append('county')
temp.append('specialty')
temp.append('state + specialty')
temp.append('county + specialty')
res.append(temp)
for index, row in enumerate(app_doctor_list):
	if(row[3] in doctor):
		temp=[]
		temp.append(row[3])
		temp.extend(doctor[row[3]])
		temp.append(row[20])
		temp.append(row[22])
		temp.append(row[29])
		temp.append(row[20]+","+row[29])
		temp.append(row[22]+","+row[29])
		res.append(temp)



wfile=open('doctor_moreinfo.csv','wb')
writer=csv.writer(wfile)
writer.writerows(res)

