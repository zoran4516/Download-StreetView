import pandas as pd
import numpy as np
import urllib,requests    
import hashlib
import os,datetime
import time
import urllib.request
import time
from urllib import error
from urllib.request import urlopen
import random 

#注意：streetscore_boston.csv文件要放在当前路径下
requestPath = './streetscore_boston.csv'
APIPath = 'api.txt'
APIURL1 = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
requestDF = pd.read_csv(requestPath)
length = len(requestDF)
apiList = list(pd.read_csv(APIPath,header=None)[0])
apiIndex = 1
APIURL2 = "https://maps.googleapis.com/maps/api/streetview?"

#选取你要下载的图片编号，我这里是163000到200000
for i in range(length)[163000:200000]:
    thisDF = requestDF.loc[i:i]
    lat = float(thisDF.latitude)
    lng = float(thisDF.longitude)
    PARAMS1 = dict(size = "400x400", location = '{},{}'.format(lat,lng), key = apiList[apiIndex])
    PARAMS2 = dict(size = "400x400", location = '{},{}'.format(lat,lng))
    url1 = APIURL1 + urllib.parse.urlencode(PARAMS1)
    url2 = APIURL2 + urllib.parse.urlencode(PARAMS2)
    response = requests.get(url1, stream=True,verify=True).json()
    status = response['status']
    res=requests.get(url2,verify=True).status_code
    if response['status'] == u'OK':
        if res == 200:
            urllib.request.urlretrieve(url2.strip(),"E:\\photo\%s.jpg"%i)
            print(i)
            print("dowmload success")
    elif status == u'OVER_QUERY_LIMIT':
        print(res)
        apiIndex+=1
           
    elif status == u'ZERO_RESULTS':
        print(status)        
    else:
        print("else")
        continue