import pandas as pd
from pandas import *

bscp = pd.read_table("bsc_pre.txt",sep=';')
bscp.to_csv("basic_prescription.csv")
bsco = pd.read_table("bsc_otc.txt",sep=';')
bsco.to_csv("basic_otc.csv")
blkp = pd.read_table("blk_pre.txt",sep=';')
blkp.to_csv("blackbox_pre.csv")
blko = pd.read_table("blk_otc.txt",sep=';')
blko.to_csv("blackbox_otc.csv")

pre = pd.read_table("file.txt",sep=';')
otc = pd.read_table("file2.txt",sep=';')

pre['drug_interact_avoid1']=''
pre['drug_interact_may_use1']=''
pre['drug_interact_high_risk1']=''
pre['drug_interact_avoid2']=''
pre['drug_interact_may_use2']=''
pre['drug_interact_high_risk2']=''
pre['drug_interact_avoid3']=''
pre['drug_interact_may_use3']=''
pre['drug_interact_high_risk3']=''

for i in pre.index:
    if pre['interact_para1'][i] == 'interact_no':
        pre['drug_interact_avoid1'][i] = pre['Interact1'][i]
    elif pre['interact_para1'][i] == 'interact_may':
        pre['drug_interact_may_use1'][i] = pre['Interact1'][i]
    elif pre['interact_para1'][i] == 'interact_risk':
         pre['drug_interact_high_risk1'][i] = pre['Interact1'][i]

for i in pre.index:
    if pre['interact_para2'][i] == 'interact_no':
        pre['drug_interact_avoid2'][i] = pre['Interact2'][i]
    elif pre['interact_para2'][i] == 'interact_may':
        pre['drug_interact_may_use2'][i] = pre['Interact2'][i]
    elif pre['interact_para2'][i] == 'interact_risk':
         pre['drug_interact_high_risk2'][i] = pre['Interact2'][i]

for i in pre.index:
    if pre['interact_para3'][i] == 'interact_no':
        pre['drug_interact_avoid3'][i] = pre['Interact3'][i]
    elif pre['interact_para3'][i] == 'interact_may':
        pre['drug_interact_may_use3'][i] = pre['Interact3'][i]
    elif pre['interact_para3'][i] == 'interact_risk':
         pre['drug_interact_high_risk3'][i] = pre['Interact3'][i]

pre['drug_interact_avoid'] = pre['drug_interact_avoid1'] + pre['drug_interact_avoid2'] + pre['drug_interact_avoid3']
pre['drug_interact_may_use'] = pre['drug_interact_may_use1'] + pre['drug_interact_may_use2'] + pre['drug_interact_may_use3']
pre['drug_interact_high_risk'] = pre['drug_interact_high_risk1'] + pre['drug_interact_high_risk2'] + pre['drug_interact_high_risk3']

#pre[[10,11,12,13,14,15,25,26,27,28,29,30,31,32,33,34,35,36]]   
p = pre[[0,1,2,3,4,5,6,7,8,9,34,35,36,16,17,18,19,20,21,22,23,24]]

otc['drug_interact_avoid1']=''
otc['drug_interact_may_use1']=''
otc['drug_interact_high_risk1']=''
otc['drug_interact_avoid2']=''
otc['drug_interact_may_use2']=''
otc['drug_interact_high_risk2']=''
otc['drug_interact_avoid3']=''
otc['drug_interact_may_use3']=''
otc['drug_interact_high_risk3']=''

for i in otc.index:
    if otc['interact_para1'][i] == 'interact_no':
        otc['drug_interact_avoid1'][i] = otc['Interact1'][i]
    elif otc['interact_para1'][i] == 'interact_may':
        otc['drug_interact_may_use1'][i] = otc['Interact1'][i]
    elif otc['interact_para1'][i] == 'interact_risk':
         otc['drug_interact_high_risk1'][i] = otc['Interact1'][i]

for i in otc.index:
    if otc['interact_para2'][i] == 'interact_no':
        otc['drug_interact_avoid2'][i] = otc['Interact2'][i]
    elif otc['interact_para2'][i] == 'interact_may':
        otc['drug_interact_may_use2'][i] = otc['Interact2'][i]
    elif otc['interact_para2'][i] == 'interact_risk':
         otc['drug_interact_high_risk2'][i] = otc['Interact2'][i]

for i in otc.index:
    if otc['interact_para3'][i] == 'interact_no':
        otc['drug_interact_avoid3'][i] = otc['Interact3'][i]
    elif otc['interact_para3'][i] == 'interact_may':
        otc['drug_interact_may_use3'][i] = otc['Interact3'][i]
    elif otc['interact_para3'][i] == 'interact_risk':
         otc['drug_interact_high_risk3'][i] = otc['Interact3'][i]

otc['drug_interact_avoid'] = otc['drug_interact_avoid1'] + otc['drug_interact_avoid2'] + otc['drug_interact_avoid3']
otc['drug_interact_may_use'] = otc['drug_interact_may_use1'] + otc['drug_interact_may_use2'] + otc['drug_interact_may_use3']
otc['drug_interact_high_risk'] = otc['drug_interact_high_risk1'] + otc['drug_interact_high_risk2'] + otc['drug_interact_high_risk3']

o = otc[[0,1,2,3,4,5,6,7,8,9,34,35,36,16,17,18,19,20,21,22,23,24]]

p.to_csv("use_prescription.csv")
o.to_csv("use_otc.csv")

