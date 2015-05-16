__author__ = 'bohdan'

import  urllib2
import pandas as pd
from os import listdir
from datetime import datetime

#change places
def replace(x):
    region=[22, 24, 23, 25, 3, 4, 8, 19, 20, 21, 9, 26, 10, 11, 12, 13, 14, 15, 16, 27, 17, 18, 6, 1, 2, 7, 5]
    return region[x-1]

#index
def index(x):
    if x<10:
        index = "0" + str(x)
    else: index = str(x)
    return index

#index2
def index2(x):
    if int(replace(x))<10:
        index2 = "0" + str(replace(x))
    else: index2 = str(replace(x))
    return index2

#seache .csv
def seache_csv(x):
    allfiles = listdir("D:/anaconda/")
    allcsv = filter(lambda x: x.endswith('.csv'), allfiles)
    return str(allcsv[x-1])

#DataFrame
def datframe(x):
    df = pd.read_csv(seache_csv(x),index_col=False, header=1)
    return df

#download files
def download():
    i = 0
    for i in range(1, 28):
        dt = datetime.strftime(datetime.now(), "%Y.%m.%d_%H.%M.%S")
        url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+index(i)+".txt"
        vhi_url = urllib2.urlopen(url)
        out = open('vhi_id_'+index2(i)+"_"+dt+'.csv','wb')
        out.write(vhi_url.read())
        out.close()
        print "VHI is downloaded..."+str(i)
        i+=1

#seache year
def year_VHI(a, year):
    b = a[a['year'] == int(year)]
    print(b.loc[:,['year', 'VHI']])

#max VHI
def max_VHI(a):
    print(a[a['VHI']==a['VHI'].max()])

#min VHI
def min_VHI(a):
    b = list()
    for e in list(a['VHI']):
        if e != -1:
            b.append(e)
    print(min(b))
    #print(a[a['VHI']==a['VHI'].min()])

#main()
download()
k = int(input())
df = datframe(k)
print(df)
year_VHI(df, 2015)
max_VHI(df)
min_VHI(df)



