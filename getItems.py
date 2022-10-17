from re import I
import requests
import json

class getItems():
    def walmartItems(self,itemSearch,storeID):

        itemSearch = 'broccoli'
        storeID = '3133'

        url = f"https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22{itemSearch}%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22broccoli%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Atrue%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Atrue%2C%22pageType%22%3A%22SearchPage%22%7D"

        payload={}
        headers = {
        'authority': 'www.walmart.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'vtc=fkwE8VRmVw-3LPBUvNgfxM; _abck=j4ghcbkkk1iuv5qb24hx_1862; ACID=6783deab-9a62-4b24-a4d5-e588fdc0666b; hasACID=true; _pxhd=316d5c7455b27df562b67b440944523aebc9a7401d75e01330feb78c4f1dd7f8:8851bd59-43aa-11ed-9e97-494754667142; TBV=7; dimensionData=939; pxcts=a2f5ad62-4b37-11ed-ad0c-564b7a737341; _pxvid=8851bd59-43aa-11ed-9e97-494754667142; auth=MTAyOTYyMDE4iiKp5NrTopjDlrUwU1z2tcONrNYiFumPS1UYpvtiyqxs%2BKC8RG4J8bntpo5jdqSF%2BgQVe0rrArzHa77vlpyLSjWOtx9gkmiYZiKnGbvhKowQcmRi6ZK3UHmFbLMwrc0w767wuZloTfhm7Wk2KcjygkeeSCv4Chv5IarMOQ7pqjdWfTH9BATfrnclOUjuedDm0o70w6NgikYOn3qtcJgcTGK0H82ifhi7ivFxwLwbe3gUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrm5%2BH7OFk5snY5qeMwazalZrKyvt84Os4oqUXIb427dEzKyJRIFmY9DiRybhtLpH0KPjHt0LFJA8yk74a1ppaaY4idXL%2BRf7%2FlyNWwZnxBX2nG3Rj7sHAaWfI2DqvK1c7JE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJQSUNLVVAiLCJwaWNrdXAiOlt7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMjI1MSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzQuMDMwNCwibG9uZ2l0dWRlIjotMTE3Ljk0MDMsInBvc3RhbENvZGUiOiI5MTc0NCIsImNpdHkiOiJMYSBQdWVudGUiLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjIyNTEiLCJkaXNwbGF5TmFtZSI6IkNpdHkgT2YgSW5kdXN0cnkgU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMjI1MSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NjU5OTY4NDcyMjMsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo2NzgzZGVhYi05YTYyLTRiMjQtYTRkNS1lNTg4ZmRjMDY2NmIifQ%3D%3D; assortmentStoreId={storeID}; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJQSUNLVVAiLCJpc0V4cGxpY2l0IjpmYWxzZSwic3RvcmVJbnRlbnQiOiJQSUNLVVAiLCJtZXJnZUZsYWciOnRydWUsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjQ4NjM2OTExMzN9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2NTk3NTI0NzIyMSwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY0ODYzNjkxMTMzLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6Njc4M2RlYWItOWE2Mi00YjI0LWE0ZDUtZTU4OGZkYzA2NjZiIn0%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; bstc=ZDrBxYKn779_q4prevlq74; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=1W06O|1ymNb|20yr2|3mpU4|5_9FA|5f4tU|9CVUZ|CQWzm|C_vdV|DJvKV|GzUv6|H9VcM|HUnA1|HjWUQ|JCPlz|JnuDC|NBAls|OH8Y5|Qz3xl|Rgq78|Rt7EL|SPL_W|SmVSa|V9eZu|XA_S7|c6tgM|c8HYq|g0dgr|hYHrN|o7VCR|opFAJ|pSCez|qb-IF|rlJqf|rtb_E|s4Kzt|sQWPT|tyeB4|tzVuW|u8ztl|udhq9|vCU7g|vTmRC|wPXtX|xI7yg|xOe2Z|xdwD5|xlLfn|y-oun; exp-ck=1ymNb320yr213mpU415_9FA2CQWzm1DJvKV1HUnA11HjWUQ1JnuDC1NBAls1Qz3xl1Rgq781Rt7EL2SmVSa1XA_S71c6tgM3c8HYq1g0dgr2opFAJ1pSCez1qb-IF3rtb_E1s4Kzt1tyeB41u8ztl1udhq91vCU7g1vTmRC1wPXtX2xdwD51y-oun1; xpkdw=1; ak_bmsc=9C9C28808354ACB980C085C3E72FEB59~000000000000000000000000000000~YAAQDVLIF75K0NiDAQAAruTc4xGwPMsDiOja0KEYWBlXqy8V7wqbw4U9As4144kYhw6MVssD/uJBi+k7A87WBlW6cxWemyl46GFQvAWVHdKRzsgxnQdF//fdtj/YNH55ZLwZxooiE2c1FF7e2wvUVrBc7xhWZpQm28ZElmrRHb76L0UJndPLGKvIQnUb9EqkMoxgI2puOHKUwXDQ+ymOhtvsUu5A08pWS9zHABC9EOERgaL/BrRs7h8vCJGTdzCHqah+q8JIngw1cdt4pKCxcxNF/Y0/DeIpbvlFwmBBaenrto9rWHBV/KEcLsCuv9VRM1jWX0zohUpJXDEResaP8dJT2qBv5N/jL3lcHZA6cotVXCH3jjctzBRVZMdFf2BIMnFIy16kKvKj8bbzv8T+DTyI8mNdi3/FEK135ttV0c+kmTGlPz2xz0WCnZwzav2yZj3T0qw1u+fen5bjjmnkvy3XWP6e4wWT9u9vIf3IXJ0=; _astc=000b0131101bd57b85394ceaac8b5797; xptc=assortmentStoreId%2B{storeID}; xptwj=cq:cc86724c1cbc0fd0e545:PgsGWdiknO/KdOfrICWBO0DQj4YT3A0totIubb6M5eulnwCFN8NacXNZjlbfwVWYALwx74liD7Gdf9lTurQ5w3cu1yP5l86HG9D25vADGku2CzOj5NWYFL4DPiwGEvVzpbGu3LTlgfMiy/vn1kCYXnqRYJI=; akavpau_p2=1665975853~id=e10b5c4546fc2009a2e0de259668ac30; bm_mi=49C2D0B5BE317A0682E4AD3C053FA044~YAAQDVLIF5ZM0NiDAQAAY/jc4xFzYFqXZzmhPOWSQyBk4bTTOhg5F2SqVHMam0KWhJhTSQnDSM2zwCd78NChgJRieXSWvc5win3j7+G+2DD4cu+fZXRv9Y6sknEfCrEC9qqd+/9FmaDQyVNSCAhCie9kcX77U/jDqr56h2+GvCyXgkCqer0jceybYgTmNq7CoB8+dwf2xAG5L3ErLTmb2zj6pPatj3cgaNnjgfKrQDQMZdMLxs5ZAmnNqOCPkU/yR8uVLZcEoraJ9IDySGjyWgGdWvH5qME+tCWvoHpToG9ZNZJWnMz2FNfdWCNTxaaipBOCSKVMBHtEx1LZE5BJi5T5vddq5auzjg==~1; adblocked=true; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1665976089000@firstcreate:1602138027142"; xptwg=1807693626:EF199E6B4F2190:268695F:8512670C:560B14D5:2008F7D1:; xpm=0%2B1665976096%2BfkwE8VRmVw-3LPBUvNgfxM~%2B0; TS012768cf=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS01a90220=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS2a5e0c5c027=08fe679738ab20003e547791d391c11d03543faee317a34af73683f67d11bed0848ec9958b14d7be08ff158dde113000b92c659176ce76552d84422c2a3dc706b2dd6b26d2ed9fe03e5891888290f521341f2b9b7adf124911b55cf35a3762fe; bm_sv=9861D1A104E457F58104513D27C61FE0~YAAQDVLIF7Gg0diDAQAAxNjp4xFoSf1OCys7PILizMWHyEhzaW/6hGQcKK51nDrysHZIHOqa7w8pMZpHlrj7hN3qUTBZFo2TUIHjR2iN62eXJFt9n4RkRXZFz+vxocm5hwQjUeUIgTqD97wif+mioH3dN5SArS20LJkycP+fJgZSVThgBK24P13Uyf4itjYQLFoic3INDjvjtDnreBngGXpr7UkcxmKktKfXXvOzhsdjExUOAX+U0cMlB2UKbVptdrQ=~1; ACID=79be637b-6d55-4198-bc7f-702c3e95f2fa; TS01a90220=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; hasACID=true; vtc=b5jNbO62qAh0b8YyVrRJ60; xptwg=1318782031:114459438E84300:2C870B8:98A8505:E75DA1FB:7A8C437A:; xptwj=cq:7bfe79cbb34b6ed83ad2:J0SmeuIggQVJ2hFqVjB+hq7CNSP895d1DIF4pCwRVhQ9tk8BsiPCN/dmdBrxDFWN7e4CKH4boZWdZ+m9z+qpCYzIs2B02zsIFaBTh1xPx83NcDKmDUcpnFrhsabUEE4=; TS012768cf=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; _pxhd=18a50fcfff40c3bebcd2538552476ffb06ba17552884265c365a7cdb84f5f040:cdb44efb-4991-11ed-84a5-7656696c4472; akavpau_p2=1665513209~id=ae7da43442a7ed36c30e32159d4a8d96',
        'device_profile_ref_id': 'Rygd3MFxnSho6KM-g8Dy0gVBmdTiP_SnnT8y',
        'referer': 'https://www.walmart.com/search?q=broccoli',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-ff829608b459efbcd79c70dc23d78aea-ccdee82fa114de4a-00',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'wm_mp': 'true',
        'wm_page_url': 'https://www.walmart.com/search?q=broccoli',
        'wm_qos.correlation_id': 'LIT9_N4_rVONMsRogxX5DEnsoF_In1bmGXbs',
        'x-apollo-operation-name': 'Search',
        'x-enable-server-timing': '1',
        'x-latency-trace': '1',
        'x-o-bu': 'WALMART-US',
        'x-o-ccm': 'server',
        'x-o-correlation-id': 'LIT9_N4_rVONMsRogxX5DEnsoF_In1bmGXbs',
        'x-o-gql-query': 'query Search',
        'x-o-mart': 'B2C',
        'x-o-platform': 'rweb',
        'x-o-platform-version': 'main-1.25.0-b626c5',
        'x-o-segment': 'oaoh'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        searchedItems = json.loads(response.text)

        items = searchedItems['data']['search']['searchResult']['itemStacks']
        itemID = {}
        itemInfo = {}

        for i in items:
            items = i 

        for num,i in enumerate(items['itemsV2']):
            itemID[num] = i['name']
            itemInfo[i['name']] = {'shortDescription' : i['shortDescription'],
                                'imageURL' : i['imageInfo']['thumbnailUrl'],
                                'currentPrice' : i['priceInfo']['currentPrice']}

        print(itemID,'\n')
        for i in itemInfo:
            print(i, '\n', itemInfo[i],'\n\n\n')
        
        return items[itemID,itemInfo]