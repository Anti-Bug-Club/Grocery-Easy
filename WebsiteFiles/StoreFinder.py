# from crypt import methods
from multiprocessing import context
from flask import request
from flask import Flask, render_template, url_for, redirect
import requests
import json
import csv
import re
from bs4 import BeautifulSoup 
from flask_bootstrap import Bootstrap
from getItems import getItems
import asyncio
import time

class getStores():
  #use any zipcode to get list of stores within 50 miles
  async def walmartStores(zipCode):
    url = "https://www.walmart.com/orchestra/home/graphql"
    radius = 5

    payload = json.dumps({
      "query": "query storeFinderNearbyNodesQuery($input:LocationInput!){nearByNodes(input:$input){nodes{id distance type isGlassEligible displayName name phoneNumber address{addressLineOne addressLineTwo state city postalCode country}capabilities{accessPointId accessPointType}open24Hours operationalHours{day start end closed}nodeDistance{unitOfMeasure value}services{displayName name phone}geoPoint{latitude longitude}}}}",
      "variables": {
        "input": {
          "postalCode": str(zipCode),
          "nodeTypes": [
            "STORE"
          ],
          "accessTypes": [
            "PICKUP_INSTORE",
            "PICKUP_CURBSIDE",
            "DELIVERY_ADDRESS",
            "DELIVERY_IN_HOME",
            "DELIVERY_SPECIAL_EVENT",
            "PICKUP_SPOKE",
            "PICKUP_BAKERY",
            "ACC"
          ],
          "radius": radius
        }
      }
    })

    #headers needed to bypass cookies and being blocked
    headers = {
      'authority': 'www.walmart.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'cookie': 'QuantumMetricUserID=bb70e4604030c4332510724b3d0fff8a; vtc=RgOWoCw-602xtfdRFHcFc4; bstc=RgOWoCw-602xtfdRFHcFc4; xpa=0NcOK|15Gwj|5_9FA|5ccTK|7LSfW|9e61f|AIud-|D2JLq|DuuJN|H9VcM|I9lIr|JYP3v|MJuLK|N8QWO|NBAls|OaWZ8|Qx0BC|Rgq78|S-Z8m|S3bS1|SPL_W|SmVSa|T-onc|Twnv9|V-nnO|VzzTL|XcRMg|XmJLH|Y9_n0|bj38K|ccDGr|d93_H|eTJXg|fXIW_|m6OsI|mM0Sa|opnnN|riTZF|s4Kzt|sQWPT|sbguX|szDEg|tWk_I|tsxuA|tzVuW|u8ztl|uccoC|uj-23|uru_L|wX6Ex|wexEY|x_hKt|xyycY|zCylr|zFeZ5|zhSyo; exp-ck=0NcOK115Gwj15_9FA27LSfW19e61f1D2JLq1JYP3v2MJuLK1NBAls1OaWZ81Qx0BC1Rgq781S-Z8m1S3bS11SmVSa1V-nnO1VzzTL3XcRMg3bj38K1ccDGr1eTJXg2m6OsI1mM0Sa1s4Kzt1sbguX1szDEg1tWk_I1u8ztl1uccoC2wexEY4x_hKt1xyycY1zFeZ51; auth=MTAyOTYyMDE4s1IcxbiuZBOYfMw%2BJBnMXLiIpMdiyvqRHqk1eyM8tL1V7qIP1yO%2BjynuVIALJDnuaDlHjhBnW44oLOp79puT%2FmKhSMEnSJHjg9fDpHgRc%2FZNqa8ifFl8hthPBla%2BlRCc767wuZloTfhm7Wk2Kcjygi5k0VvBM%2FJjwcKWWhCnBS9C699Z9sWpnpMNQKz%2BtNJ7wSkTy7fSX9t8kxPSo5mc6AndG31iONUJT80ft8%2BD1F4UMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKriRfksaLmPBsejyAY9U4Hnx04tmf7HLyxOhjXnh5eUNKQpRRL0GhWOWqWRJScUqmtVUUYiBV89OSmqbI1CZKMyw8fvjmv7%2BXkAndPM6uDQ5FtHSA%2BGqjd0ktX0ovfExbI5E5WBBdZBCyKnCQAR7o6eg%3D; ACID=77bff0ac-1fd3-4a3f-81ba-7170e5412c85; hasACID=true; assortmentStoreId=2251; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; mobileweb=0; xpth=x-o-mverified%2Bfalse; _pxhd=ee15809879106935c0e82876c10b319cd3bcf1df5b15e4726a43cc50a6380c14:ac44aa5f-41d1-11ed-9720-66675a737546; bm_mi=3D2BB5421BEB53060A7038B44AB3561B~YAAQn8POF+YCp4KDAQAA22J+lRHwDOEmRk/gr3GXoB2JV8NxHiFATNXI3nGis5xewXoOsm/yJaNpd9RoJdJ2h17ME4tsFfnJd8Eu2LXA+uhcPtATUAkDHdqU0eEI1i9yS2WaIKxheCXmw96F75wDSxZt9NdV0pJWPYH13cifnXSrpJTBoP+G2lsdMm4qn6YqfTwSIJqRuuFEE79RJuIcHGehdH8EIEpgtp+3UXe/ooFleT9cJ3uC0f6zveg+FIzNo5W05olOJS4krHn50yNT/ebwPJLg0+sUR9/ePjN0x0LJBUajCT5aGuq0EpDgmlb03ua4VdDiWJWqlFE=~1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9TUEVDSUFMX0VWRU5UIiwiUElDS1VQX0JBS0VSWSIsIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2NDY4MjAzMjk5NywidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjc3YmZmMGFjLTFmZDMtNGEzZi04MWJhLTcxNzBlNTQxMmM4NSJ9; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMjI1MSIsInRpbWVzdGFtcCI6MTY2NDY2MDQzMjk5NH0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY0NjYwNDMyOTk0LCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NzdiZmYwYWMtMWZkMy00YTNmLTgxYmEtNzE3MGU1NDEyYzg1In0%3D; xptc=assortmentStoreId%2B2251; _astc=68e12af5a2485f61a9640813d9494eb6; pxcts=ad8657d1-41d1-11ed-8e62-4e496d557677; _pxvid=ac44aa5f-41d1-11ed-9720-66675a737546; TBV=7; _px3=bf7def05c09792d2da5d62d5d6b994ed27d4ae901c5d58795dd757d21c9484ab:OXSfmthNeLqa15AncTfXsCce6GnoFX7RGUshw7O9Z1g8pA7pB7mF1+16opQVHz6xYWGSZBBDbszRUxjOdoxWRg==:1000:83SA5rGKJOc9TL07KQA0rXgdlqwT32jI6notML0vNZIOHQ2pPXqomNSGJP+mNbC1WptTt9KTFukHZRc2VnyQquI6fZJHfDmE0mVhbkOyehbaH+H9Z/VZMK48Zk4Y3VlS4Q/urYmrLoWs/247QWhqmQFlZFmZ03VGZeYhPdPl/0UL5qMu5Lq7Dt6vHXd1mBZvw/MsR8I9V3jZMr8ZCHhWbg==; ak_bmsc=F9ED04FEA1711D31EB91CA2E34FB8A1B~000000000000000000000000000000~YAAQn8POF4ADp4KDAQAAQHN+lRGFrPwn5mkJpK06PCkLFFaC4Kue52FJLU8MfU9nOgA15nLmkQqZAB+RNIfx1v+xNZqgCjgbw/YgcilFRqSUWo8Vwn89HvN397Bv0OizSKEOvVJqurlfEvo2a0WP5reXrOBlo3KQB7XUtjr//6SmeEeg3F0v1cZ1vLHHEChOCpl1XjZ3UN8PZHKdUOMzII4Cyw0mtVyIWIPBYYI7gd4MZBKj0EePQDqwo8FkLDUkwfME02qFMwE6/GC3Lnnz/g4yZg1MaT/wDL/KD7VWqlbZGxfFW1dpGcNze1P8S0zXgsTl3Yy04vB3Buokvqj+/JHMCpQ2/KzkVXG2Vd7zJQL7kGS7Jkog54JIhOh3hlJmLjbpf1bD8RYqLKKetPGT1zYJ+4Akj9GMEkBDllsaVV8F9fcVw9V/LlI=; xpm=0%2B1664660510%2BRgOWoCw-602xtfdRFHcFc4~%2B0; xptwj=cq:8b3db665c558250cdb54:sWuyofl5reQuPw7EwLoSDyexTobjFbTFtyOOP5WBzeBkWzaGxj8LWtBRuqeDa9JdhKraofoZB7OZ6OHDqHE15avx/K550eVAnIpy+9qXMZu/NUmRUw==; xptwg=330554976:1C71EEB8FAEBD90:4964032:CE94FAB:32D85087:787F6CB5:; TS012768cf=019c4a6c416fe3d39202a9a9b88b479842fef3c14cb190c74cc1079339d6e1c698bd4e19f2ef129c4197c498f6a454a2f00e6b3d1b; TS01a90220=019c4a6c416fe3d39202a9a9b88b479842fef3c14cb190c74cc1079339d6e1c698bd4e19f2ef129c4197c498f6a454a2f00e6b3d1b; TS2a5e0c5c027=083ee07ae4ab2000b17c67228bf5e5627549b5c42f463c0d8575f88bc440e829c0d6c49f88f4cf6d083434bd72113000baaa2bf3afdfd80fce04134076b1be8b299bc5d9d60cb5409e336c6ff32a331243e69932c719a00db77187e4fca2b47d; bm_sv=7CE60C60F5D51B3DFDDD867C1350662F~YAAQpcPOF8o55muDAQAAcJh/lRGQzdreDrP/152vQ+JaIzhVO4hKeqpqp5Gd+jSEuX/sFW7NFPqPwnjxPZhN5YEdKDICvNlFSxteii4MnEr8LEGcqPYlEyCd7wTHl3cY7DURY31+dV9sy1dha+60zjfChxUwbTr2n3aSbbJQ+Muu9vYKr0+J7iIZrI1g8demsK21VLrqa0uMBal+uF+UjbpoBSiItKFpZ4hMv15XAjmMI6zeVGzt0wHbSsHWIZjz1w==~1; TB_SFOU-100=; TS01a90220=010715e2f7d34bffcbaa14d186af13929ac693ba984659206365c9bafedd4e661f323a845c642b9bfeb895ca5a597631bc6e43fa93; bm_sv=7CE60C60F5D51B3DFDDD867C1350662F~YAAQl8POFy8gTYmDAQAAYH6HlRGHlkUvV78nkWCoctBphhiHn7lAbkusvW5e+6NQH73fYvBQ+H+8Ag0/4wfrcLTLAoPrKUE14RI/8zR8OHhmju5tE04CFUXhKJZXR+MpQCvXlK2o8vsy80Uyj6E8JOZH2aI0uN4bQLNny/P6qBSboWgfX/0Q0YiWX1j3nSSR6S/+AkZ27WrV9cVklD5sUGL63COBedC9ZF3IJtQ+O7XFw0t/OmY06K6OQdk4jG22Tg==~1; bstc=RgOWoCw-602xtfdRFHcFc4; exp-ck=0NcOK115Gwj15_9FA27LSfW19e61f1D2JLq1JYP3v2MJuLK1NBAls1OaWZ81Qx0BC1Rgq781S-Z8m1S3bS11SmVSa1V-nnO1VzzTL3XcRMg3bj38K1ccDGr1eTJXg2m6OsI1mM0Sa1s4Kzt1sbguX1szDEg1tWk_I1u8ztl1uccoC2wexEY4x_hKt1xyycY1zFeZ51; mobileweb=0; vtc=RgOWoCw-602xtfdRFHcFc4; xpa=0NcOK|15Gwj|5_9FA|5ccTK|7LSfW|9e61f|AIud-|D2JLq|DuuJN|H9VcM|I9lIr|JYP3v|MJuLK|N8QWO|NBAls|OaWZ8|Qx0BC|Rgq78|S-Z8m|S3bS1|SPL_W|SmVSa|T-onc|Twnv9|V-nnO|VzzTL|XcRMg|XmJLH|Y9_n0|bj38K|ccDGr|d93_H|eTJXg|fXIW_|m6OsI|mM0Sa|opnnN|riTZF|s4Kzt|sQWPT|sbguX|szDEg|tWk_I|tsxuA|tzVuW|u8ztl|uccoC|uj-23|uru_L|wX6Ex|wexEY|x_hKt|xyycY|zCylr|zFeZ5|zhSyo; xpm=0%2B1664661028%2BRgOWoCw-602xtfdRFHcFc4~%2B0; xptc=assortmentStoreId%2B2251; xpth=x-o-mverified%2Bfalse; xptwg=3840698849:1C7F33EB8DF1CA0:49863EB:7F0BFE5C:90641201:C554EFB9:; TS012768cf=010715e2f7d34bffcbaa14d186af13929ac693ba984659206365c9bafedd4e661f323a845c642b9bfeb895ca5a597631bc6e43fa93; TS2a5e0c5c027=08981fe414ab200022e33a2054393452b4cda392be77dc56b39e4995ea63d1b2309dea2f0b20900608e9b5cc0e11300042b7c73e9acf34625166d82707bdff53f2e4ac390655b2992e14479ef97398b21e5d4477a0faae4f81ec81263da86ec6',
      'device_profile_ref_id': 'T0CyA4hmU3DnxKuTI_HRR5_tuDVoL4MIwEQc',
      'origin': 'https://www.walmart.com',
      'referer': 'https://www.walmart.com/store-finder?location=' + str(zipCode),
      'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'traceparent': '00-f38d35c10cfe4c1be00964b9be6f2236-fdd063642f01f843-00',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
      'wm_mp': 'true',
      'wm_page_url': 'https://www.walmart.com/store-finder?location=' + str(zipCode),
      'wm_qos.correlation_id': 'pKjQt0FY1bvLdg3urY7vi6toDrn91EaK3Zq9',
      'x-apollo-operation-name': 'storeFinderNearbyNodesQuery',
      'x-enable-server-timing': '1',
      'x-latency-trace': '1',
      'x-o-bu': 'WALMART-US',
      'x-o-ccm': 'server',
      'x-o-correlation-id': 'pKjQt0FY1bvLdg3urY7vi6toDrn91EaK3Zq9',
      'x-o-gql-query': 'query storeFinderNearbyNodesQuery',
      'x-o-mart': 'B2C',
      'x-o-platform': 'rweb',
      'x-o-platform-version': 'main-1.23.0-4561b3',
      'x-o-segment': 'oaoh'
    }

    #Request store list from url 
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)

    #Set data to dictionary format
    stores = json.loads(response.text)


    closestStoresID = {}
    closestStoresInfo = {}
    for num,location in enumerate(stores['data']['nearByNodes']['nodes']):
      closestStoresID[num] = location['id']
      closestStoresInfo[location['id']] = location['address']



    # print(closestStoresID)   #you can use closestStoresID to find the address of the store locations
    # for i in closestStoresInfo:
    #   print(i,'\n',closestStoresInfo[i],'\n\n') #EX: To find the second closest store do closestStoresInfo[closestStoresID['1']]

    #BUG Here
    # itemSearch = getItems()
    # walmartSearch = itemSearch.walmartItems('broccoli', '3133') #(Item Search, StoreID)
    # print(walmartSearch)
    
    return closestStoresInfo  #Return all the closest walmart stores found

  async def targetStores(zipCode):
      url = "https://redsky.target.com/redsky_aggregations/v1/web_platform/nearby_stores_v1?limit=20&within=100&place=" + str(zipCode) + "&key=8df66ea1e1fc070a6ea99e942431c9cd67a80f02&channel=WEB&page=%2Fs%2F"
      payload={}
      headers = {
        'authority': 'redsky.target.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'TealeafAkaSid=3Yc2hZo4wdDLVmdHZNVs6bkmyn0Gxiok; visitorId=0184C64336400201BE6378F3B11880D6; sapphire=1; UserLocation=91790|34.070|-117.950|CA|US; egsSessionId=2ef64ca4-d651-40c5-b220-c22b0bf60fdd; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4NzFiZWY2Ni04NGQyLTRkODMtYWFiZC0yYmQzMWUwMGU3YWMiLCJpc3MiOiJNSTYiLCJleHAiOjE2Njk4NjAwMDUsImlhdCI6MTY2OTc3MzYwNSwianRpIjoiVEdULmU1Y2ZiOGE0NjQ2NDRmODJhOTMxODBlZWM4Yjg0Y2NhLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjZmOTQ1MWQzMTRlNzI0ZjA1NWVlMDg4MTJiYTg1ZTIyYjBjNmE3ZGY3MWU4MGUxMDlmNWNiZGMyY2VjOTU1ZTkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.peOvj-yoUv16-zvOUtICK5l5mS0N1XfaxTfkqrG2-EuB6gzuXd8UL7sR3n15Kc_mTZ7-9gPSveRG97kgtbvisSbvBa2-duS2lKoGPWcNamnz6nvmisGqwvHA3LiMl9MbP4QYSfDuKcH9aBRhMs7qm8mUs4Gw1Cw67VeDFpWoDbX8sf21dhSOoSqi7d6V0HcW6BfcTWntdvUZ_z1fsBoiblnhA_c4SioI_wm_LCFmTYyj5xF4oTBMWpKnu874LD0qCZ1LcjdMnPJOW_xW-mQ01ZKXyYCGrseLIiw0ivjvoKb7Nzfd-3ZpDZlGSyY-clqBwcJYtosjbIVwHOdQf0foOQ; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiI4NzFiZWY2Ni04NGQyLTRkODMtYWFiZC0yYmQzMWUwMGU3YWMiLCJpc3MiOiJNSTYiLCJleHAiOjE2Njk4NjAwMDUsImlhdCI6MTY2OTc3MzYwNSwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=dBQs2t5KTNdlYOvvmtvK9crePp9m5O64tlTr13uVEcsif_x0-A7xKiSiW5IamzQhcnUsmCCJzaC1SkfWANFIYg; fiatsCookie=DSI_1033|DSN_Baldwin%20Park|DSZ_91706; __gads=ID=9dc0e100053d6526:T=1669773605:S=ALNI_MYbTgL-doQ2Z2njBhmLgLu_DwHzqg; __gpi=UID=0000090805556266:T=1669773605:RT=1669773605:S=ALNI_MbrHnmao9jxdJuHWJmnUdg01mpM6g; _mitata=M2Q1NjNjZjZjZWJkYzljYjI0M2E5NTFlZmZlY2MwZWZmY2E4ZDc1ZTczODBhNWY5YTUwY2EwMTAxZDE1NjZkMg==_/@#/1669774112_/@#/crteAngtSv6P95p5_/@#/NDQ1MmFlZDgwOGE3ZjAxYWE5OWYxZTg4MGNmMDkxNTNkODA5ZGJiZDVlYmFmOTI2Y2MxOWYxNDY2ZGQ3YTgzNg==_/@#/000; ffsession={%22sessionHash%22:%2263d55700f64f91669773605935%22%2C%22prevPageName%22:%22store%20locator:%20find%20stores%22%2C%22prevPageType%22:%22store%20locator%22%2C%22prevPageUrl%22:%22https://www.target.com/store-locator/find-stores%22%2C%22sessionHit%22:13}; _mitata=ZmJiMGY4MzBiODkyMDdmYWE0MzcxN2ZkOTg2NWMxYzdlMjA5NThmNDBiNTNlOWZhMzYxOWVmZjcyYmUxZjZhZg==_/@#/1669775209_/@#/crteAngtSv6P95p5_/@#/M2Y3NjQ4M2U5Mjc3YmQzNDU4ZTIwNTQyYTk4OGU5M2FlNDdlOWJjZmUxNDE0YTU4NmFlMWE5MTdlYjc5YmUxZg==_/@#/000',
        'origin': 'https://www.target.com',
        'referer': 'https://www.target.com/store-locator/find-stores/los%20angeles,ca',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      print(response.text)

  async def walmartStoreItems(item, storeIDs):
    #Item searched at specfic store id 
    itemSearch = getItems()
    walmartSearch = {}

    #Key is store ID and Value is items 
    for storeID in storeIDs:
       walmartSearch[storeID]= itemSearch.walmartItems(item, storeID) 
    
    #Print results    
    for key, value in walmartSearch.items():   #Keys and values of walmartSearch
      print("Key= " + key, " : Val= ", value)
         
itemSearch = getItems()

app =   Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')  #render index.html file 

@app.route('/search')
def getItems():
  item = request.args.get('item', 'broccoli')
  store = request.args.get('store', '3133')
  walmartSearch = itemSearch.walmartItems(item, store)
  return render_template('index.html', items = walmartSearch)

@app.route('/products1.html') #render products.html 
def products1():
  return render_template('products1.html')
  
@app.route('/zipCode/<string:x>', methods =['GET']) #get zipcode to find closest stores
async def stores(x):
  x = json.loads(x)
  print(x)
  walmartStores =  await getStores.walmartStores(x)
  targetStores = await getStores.targetStores(x)

  # return walmartStores
  storesData = []
  stores = {
   "k" : list(walmartStores.keys()),
   "v" : list(walmartStores.values())
  }
  storesData.append(stores)
  #time.sleep(1)
  return render_template('index.html', data = storesData,)

if __name__=='__main__':
    app.run(debug=True)
