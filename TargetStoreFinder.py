from email import header
from urllib import response
from wsgiref import headers
import pandas as pd
import pymongo
import requests
import lxml
import csv
import json
import re
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bson.json_util import dumps

url='https://www.walmart.com/store/finder?location=91744&distance=50'
payload = {'nbrOfStores': 50}
requestParams = {'geoPoint': {'latitude': 34.0274622, 'longitude': -117.9307584}}

#headers needed to bypass cookies and being blocked
headers = {
'authority': 'www.walmart.com',
'method': 'GET',
'path': '/store/finder/electrode/api/stores?singleLineAddr=91744&distance=50',
'scheme': 'https',
'accept': '*/*',
# 'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json',
'cookie': 'vtc=cXlniSXtbK1T2PM4AXEUlM; _pxhd=d346de2b2ae1e475007464b61c9307a852865d2e483fbb01b0c57e2437b9c2e5:50b59251-389d-11ed-a773-59766874617a; TBV=7; _pxvid=50b59251-389d-11ed-a773-59766874617a; _gcl_au=1.1.80164407.1663648386; ACID=a88c1d44-26d9-4549-bb53-0485034b52ef; hasACID=true; __gads=ID=d96fdaf4a185b978:T=1663648466:S=ALNI_MYS7g4pvpCn4h8RgupIIHiPKMvZaQ; s_pers_2=om_mv3d%3Dsem%3Aadid-22222222254421687451%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1663911275565%3B+om_mv7d%3Dsem%3Aadid-22222222254421687451%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1664256875566%3B+om_mv14d%3Dsem%3Aadid-22222222254421687451%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1664861675567%3B+om_mv30d%3Dsem%3Aadid-22222222254421687451%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1666244075568%3BuseVTC%3DY%7C1726763630; DL=91744%2C%2C%2Cip%2C91744%2C%2C; t-loc-zip=1663648831386|91744; adblocked=false; dimensionData=1340; locGuestData=eyJpbnRlbnQiOiJQSUNLVVAiLCJpc0V4cGxpY2l0Ijp0cnVlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6dHJ1ZSwiaXNEZWZhdWx0ZWQiOmZhbHNlLCJwaWNrdXAiOnsibm9kZUlkIjoiMjI1MSIsInRpbWVzdGFtcCI6MTY2MzgyNTgxOTAwNn0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjYzODIwNTgwNTk2LCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YTg4YzFkNDQtMjZkOS00NTQ5LWJiNTMtMDQ4NTAzNGI1MmVmIn0%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; next-day=1664674200|true|false|1664712000|1664649840; location-data=91744%3ALa%20Puente%3ACA%3A%3A8%3A1|2f1%3B%3B1.75%2C1qj%3B%3B2.01%2C2pu%3B%3B3.6%2C4le%3B%3B4.04%2C1ro%3B%3B5.33%2C3oa%3B%3B7.19%2C4cp%3B%3B7.69%2C1up%3B%3B7.97%2C2i8%3B%3B8.05%2C1hx%3B%3B8.59||7|1|1ypm%3B16%3B7%3B7.69%2C1yjj%3B16%3B11%3B9.3%2C1ydp%3B16%3B12%3B12.27%2C1y7j%3B16%3B13%3B13.33%2C1yrb%3B16%3B14%3B13.43; bstc=XguKczWcjIEGBvOCz4nKtQ; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=0NcOK|15Gwj|4-FVr|5q86Y|6VwPb|6r4vW|9T1D1|AIud-|BrNRv|CShcr|DAgi2|DuuJN|FHbq-|I9lIr|K2IBM|KVFRn|LTD5Y|MQ6mX|OaWZ8|PTT2d|QB66I|RWwzc|S3bS1|SKXNG|Sf0l7|T-onc|Tk5kr|Twnv9|XA7Ad|XmJLH|ZCMn_|b5MdK|bj38K|buiiw|cL8HI|c_jjc|cfVAR|d93_H|eTJXg|ebwX-|h4oOZ|jP_Rt|lnNfN|mM0Sa|mk3nQ|opnnN|plL2z|qiczr|qouhB|riTZF|rlJqf|tWk_I|u8ztl|uZnYU|uccoC|uj-23|vuySs|w_GEw|xOe2Z|xyycY|zCylr|zFeZ5; exp-ck=0NcOK115Gwj1DAgi21FHbq-1K2IBM1MQ6mX1OaWZ81PTT2d1QB66I1RWwzc3S3bS11Sf0l71Tk5kr1XA7Ad2b5MdK3bj38K1cL8HI1eTJXg2mM0Sa1mk3nQ2plL2z1qouhB2tWk_I1u8ztl1uccoC2vuySs1w_GEw1xyycY1zFeZ51; xpm=1%2B1664649840%2BcXlniSXtbK1T2PM4AXEUlM~%2B0; pxcts=04a3f1c3-41b9-11ed-8d6b-44686d4d5279; ndcache=d; bm_mi=624F0EA07C50A68DDC259787A11F0C67~YAAQpMPOFw357HyDAQAAas/clBHDCUGC7hRP3lf4rbxSbOkNnkQl29SDEceTyM/G8dG1Eag14NY7uJiwJXTX2OphR+Bj14hy5VxZ8ovvdu6kBKe5+MFXxPSbIkCFsc9AZfvt8/d5eIHIfwCBMvArTSa044arK/wqgPnMqKvMQkd7buIUNtB4psGN9dwnbHygqero71lwJCidFbyaBBmx+oYowY9AUmxKID4WrQKUhTkC4L8oKYSE0jHTr7zzxwzUkZcM3xSZuyYjQBnomnOGpLiQirhvCQ4WHUKXv+gLX+yuMlZDqgWtRS8s/FSdLH6Zos2Tz3M5xb7rINEUt2c5CMnd+qsOO00RNQGM/MoxhQNV2Vjn3YNmYg==~1; _clck=1cj93a0|1|f5c|0; ak_bmsc=899AB8920A2B4A60D10F8E794FA66DD3~000000000000000000000000000000~YAAQpMPOFwf+7HyDAQAA+STdlBEVsbO+ATveYjkrfTkVseB7X5IZJIj59xbcjAmfFqBEAfch2VL6ENqplNN0yibo47VCV3exxDIkmOHo5Uk0ZmyEa2nG/4GqxkhUTVdVM24rttrNC7aRyDiPw/Jbbyu5JZILmvoOFI46hyB8k4d9ggoomla4nZ4wsgAsbqm+6dzwwA2juFOxmH4YFn8DJ5nmhbte8YFjRnaGOQpl/af6PvjePzVd/lQE8pr3t4A7zvTvYiboqHXSe6aCJfWFP2Xkja73QUWGw/AUItxKf5E9lywi63AL/NgNoP3AvCo+PipSz4Xc3IABCzZSb328A0CaNhqc8dYBpLK1unc9+ux27W147d+hkGbzlg4/T7bpHn043Tkvf7M8K4bS2pUaoiXEvA195o3lB8g27svQ0yJFFyPrWmA+XWmJX4DhB7qIb4EuG0D4mK2nzFf4A9kebkBV5Vfa2pqDYRD05+6hDBcWe6E/oKlV3gSwagJdceqmVMzXYTTEfQwf+ZQ0MLAeYHAZv0vYC9+p93hUZZAlfLqBq27uWepn2LeSTQ==; __gpi=UID=000008c5a1c7c764:T=1663648466:RT=1664649907:S=ALNI_MaQhpWP0d_Kx3wADSkKTCUt2ZGyaQ; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1664649948660@firstcreate:1664434158361"; xptwg=4141775420:18E222D6564D220:40339A7:DA0C89F7:6C432D5C:79ED2F0B:; xptwj=cq:d64e65645b10eb6b5159:kkDGXibayLYvhnkwBitTfkX7DEuzVLp2aWscYJNUJBOoDUHEiV3rbhBBpekaqzN87LQlp6T7wJ6sYekfuWtwuGran2nN7uGVRkw0zC983jF4i8Nt1hVA3eIAprs=; TS012768cf=01883d697b9610c0267f692c57b54a91c0ff467251a2b08bac3802599f16078486cbf821dcc70fc234c4f5707badf8fbb22d8189ba; TS01a90220=01883d697b9610c0267f692c57b54a91c0ff467251a2b08bac3802599f16078486cbf821dcc70fc234c4f5707badf8fbb22d8189ba; TS2a5e0c5c027=08d1b43516ab20001eaba12bb6e47673eada4ba31e4d62a0ff35b923b0af389c680d7e4c20d398ce08d4af705d113000c201f8808d3df514ced4c1e8177c52e02f9e3219a8a55c7689538a89ed694292176598cac181d6c35a16153b2dbc34c9; bm_sv=A47C778AB81DA0B00F6F071756E4F139~YAAQpMPOFwIW7XyDAQAAjXPelBExgFDB3X8shdoR+Sj44z/Qks0VZkneWS9ORTohF7gMDvVmDgDIjoLaJzV8RbxY75mKdT+F5JW/lrMuZ25SyqhVrfkq+0AQ5GBhrDUwjy2ifdd10JFgJ9hoJe+bT6aiTkXT/6BQYwWqRzAJnHkMxcHkV74p+L6VTTpaO2Mc1f9YXWwR3mUfVfCYOdqLUpYKcQv6Im4x74mnI002BOeiyCfYw+bfLqd2Mreotaotrg==~1; _uetsid=0526585041b911edbe94fb65a8f1fb7e; _uetvid=5258dcf0389d11edb337a5f3edef643a; _clsk=sq2u0l|1664649950659|5|0|f.clarity.ms/collect; _px3=a614ba0ab818897e8903bc7ba909c6c989e7a1dd482c206fd36b40b159b8cbca:r+LptSVyW+l4dPL8TG5HyH8iA0lNrLb8WatvAiv53zphpP4smBalw55cAl7BVNlhbklDQEzdbclxgk5+zAUrUw==:1000:3eiUfos4HjfRe/2e6bvu5RH3vXX9SqagEJc7HkJjJSZe7edOBp/djWAtJbByOKbWm2WxDWU0BSaTuB0Xnj2da9yGg+CWxExSfk/tbX86rcNnfmUq7TqjqUn3FOVbXHdTj808vqidekMmDwHNUlhJCLE5wgVY8gbuOgemvaiqD0lsTOL6cmpny8Ev4oalUuHlDymKl5Q0yJYLWlkEJKwC0w==',
'referer': 'https://www.walmart.com/store/finder?location=91744&distance=50',
'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'wm_qos.correlation_id': '814453e1-a905-40da-b8f4-613553706051',
}

response = requests.request("GET", url,headers=headers, data=payload, params=requestParams)
# print(response.text.encode('utf8'))

# Use BeautifulSoup to nicely prase response text 
soup = BeautifulSoup(response.text)
stores = soup.prettify()
print(stores)
# print(type(stores))

