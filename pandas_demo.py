import pandas as pd
import numpy as np

df=pd.read_csv('resources/云南省普通高等学校名单（本科）.csv')
siteInfo = []
for (name, url) in df[['学校名称','门户网站网址']].values:
    siteInfo.append({'name':name, 'url':url})
# only use first n for testing
# siteInfo = siteInfo[:10]
print(siteInfo)

