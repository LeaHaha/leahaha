import csv

"""
read csv 
"""
def read_csv(input_csv):
	file=open(input_csv,"rU")
	reader=csv.reader(file,dialect ='excel')
	return reader

"""
build dict for ids 
"""
def build_dict_ids(input_list):
	res=dict()
	for index, row in enumerate(input_list):
		if index !=0:
			if row[1]!="":
				res[row[0]]=row[1]

	return res


"""
generate 2D-array
"""
def create_ouput(input_list,ids_dict):
	ge=[]
	for index, row in enumerate(input_list):
		if index!=0:
			if row[2]!="":
				if int(float(row[2]))==-6:
					continue;
				else:
					if row[0] in ids_dict:
						temp=[ids_dict[row[0]],row[1],row[2],row[3],row[5],row[6],row[7]]
						ge.append(temp)
		else:
			temp=["npi","bn","claim_count","claim_count_daw1","quantity_sum","day_supply","cost_sum"]
			ge.append(temp)

	return ge

							  
def main(input_csv_1,input_csv_2):
	ge_65=read_csv(input_csv1)
	ids=read_csv(input_csv_2)

	ids_dict=build_dict_ids(ids)
	res=create_ouput(ge_65,ids_dict) 

	wfile=open('npi_priscribing.csv','wb')
	writer=csv.writer(wfile)
	writer.writerows(res)


							  
							  
if __name__ == '__main__':
							  
	input_csv1="ge65_r.csv"
	input_csv2="ids_2011.csv"
	main(input_csv1,input_csv2)

