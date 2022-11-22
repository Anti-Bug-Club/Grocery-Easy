from re import I
import requests
import json

class getItems():
    def walmartItems(self,itemSearch,storeID):
        # url = "https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22{itemSearch}%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22broccoli%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Atrue%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Atrue%2C%22pageType%22%3A%22SearchPage%22%7D"

        # payload={}
        # headers = {
        # 'authority': 'www.walmart.com',
        # 'accept': 'application/json',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'content-type': 'application/json',
        # 'cookie': 'vtc=fkwE8VRmVw-3LPBUvNgfxM; _abck=j4ghcbkkk1iuv5qb24hx_1862; ACID=6783deab-9a62-4b24-a4d5-e588fdc0666b; hasACID=true; _pxhd=316d5c7455b27df562b67b440944523aebc9a7401d75e01330feb78c4f1dd7f8:8851bd59-43aa-11ed-9e97-494754667142; TBV=7; dimensionData=939; pxcts=a2f5ad62-4b37-11ed-ad0c-564b7a737341; _pxvid=8851bd59-43aa-11ed-9e97-494754667142; auth=MTAyOTYyMDE4iiKp5NrTopjDlrUwU1z2tcONrNYiFumPS1UYpvtiyqxs%2BKC8RG4J8bntpo5jdqSF%2BgQVe0rrArzHa77vlpyLSjWOtx9gkmiYZiKnGbvhKowQcmRi6ZK3UHmFbLMwrc0w767wuZloTfhm7Wk2KcjygkeeSCv4Chv5IarMOQ7pqjdWfTH9BATfrnclOUjuedDm0o70w6NgikYOn3qtcJgcTGK0H82ifhi7ivFxwLwbe3gUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrm5%2BH7OFk5snY5qeMwazalZrKyvt84Os4oqUXIb427dEzKyJRIFmY9DiRybhtLpH0KPjHt0LFJA8yk74a1ppaaY4idXL%2BRf7%2FlyNWwZnxBX2nG3Rj7sHAaWfI2DqvK1c7JE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJQSUNLVVAiLCJwaWNrdXAiOlt7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMjI1MSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzQuMDMwNCwibG9uZ2l0dWRlIjotMTE3Ljk0MDMsInBvc3RhbENvZGUiOiI5MTc0NCIsImNpdHkiOiJMYSBQdWVudGUiLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjIyNTEiLCJkaXNwbGF5TmFtZSI6IkNpdHkgT2YgSW5kdXN0cnkgU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMjI1MSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NjU5OTY4NDcyMjMsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo2NzgzZGVhYi05YTYyLTRiMjQtYTRkNS1lNTg4ZmRjMDY2NmIifQ%3D%3D; assortmentStoreId={storeID}; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJQSUNLVVAiLCJpc0V4cGxpY2l0IjpmYWxzZSwic3RvcmVJbnRlbnQiOiJQSUNLVVAiLCJtZXJnZUZsYWciOnRydWUsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjQ4NjM2OTExMzN9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2NTk3NTI0NzIyMSwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY0ODYzNjkxMTMzLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6Njc4M2RlYWItOWE2Mi00YjI0LWE0ZDUtZTU4OGZkYzA2NjZiIn0%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; bstc=ZDrBxYKn779_q4prevlq74; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=1W06O|1ymNb|20yr2|3mpU4|5_9FA|5f4tU|9CVUZ|CQWzm|C_vdV|DJvKV|GzUv6|H9VcM|HUnA1|HjWUQ|JCPlz|JnuDC|NBAls|OH8Y5|Qz3xl|Rgq78|Rt7EL|SPL_W|SmVSa|V9eZu|XA_S7|c6tgM|c8HYq|g0dgr|hYHrN|o7VCR|opFAJ|pSCez|qb-IF|rlJqf|rtb_E|s4Kzt|sQWPT|tyeB4|tzVuW|u8ztl|udhq9|vCU7g|vTmRC|wPXtX|xI7yg|xOe2Z|xdwD5|xlLfn|y-oun; exp-ck=1ymNb320yr213mpU415_9FA2CQWzm1DJvKV1HUnA11HjWUQ1JnuDC1NBAls1Qz3xl1Rgq781Rt7EL2SmVSa1XA_S71c6tgM3c8HYq1g0dgr2opFAJ1pSCez1qb-IF3rtb_E1s4Kzt1tyeB41u8ztl1udhq91vCU7g1vTmRC1wPXtX2xdwD51y-oun1; xpkdw=1; ak_bmsc=9C9C28808354ACB980C085C3E72FEB59~000000000000000000000000000000~YAAQDVLIF75K0NiDAQAAruTc4xGwPMsDiOja0KEYWBlXqy8V7wqbw4U9As4144kYhw6MVssD/uJBi+k7A87WBlW6cxWemyl46GFQvAWVHdKRzsgxnQdF//fdtj/YNH55ZLwZxooiE2c1FF7e2wvUVrBc7xhWZpQm28ZElmrRHb76L0UJndPLGKvIQnUb9EqkMoxgI2puOHKUwXDQ+ymOhtvsUu5A08pWS9zHABC9EOERgaL/BrRs7h8vCJGTdzCHqah+q8JIngw1cdt4pKCxcxNF/Y0/DeIpbvlFwmBBaenrto9rWHBV/KEcLsCuv9VRM1jWX0zohUpJXDEResaP8dJT2qBv5N/jL3lcHZA6cotVXCH3jjctzBRVZMdFf2BIMnFIy16kKvKj8bbzv8T+DTyI8mNdi3/FEK135ttV0c+kmTGlPz2xz0WCnZwzav2yZj3T0qw1u+fen5bjjmnkvy3XWP6e4wWT9u9vIf3IXJ0=; _astc=000b0131101bd57b85394ceaac8b5797; xptc=assortmentStoreId%2B{storeID}; xptwj=cq:cc86724c1cbc0fd0e545:PgsGWdiknO/KdOfrICWBO0DQj4YT3A0totIubb6M5eulnwCFN8NacXNZjlbfwVWYALwx74liD7Gdf9lTurQ5w3cu1yP5l86HG9D25vADGku2CzOj5NWYFL4DPiwGEvVzpbGu3LTlgfMiy/vn1kCYXnqRYJI=; akavpau_p2=1665975853~id=e10b5c4546fc2009a2e0de259668ac30; bm_mi=49C2D0B5BE317A0682E4AD3C053FA044~YAAQDVLIF5ZM0NiDAQAAY/jc4xFzYFqXZzmhPOWSQyBk4bTTOhg5F2SqVHMam0KWhJhTSQnDSM2zwCd78NChgJRieXSWvc5win3j7+G+2DD4cu+fZXRv9Y6sknEfCrEC9qqd+/9FmaDQyVNSCAhCie9kcX77U/jDqr56h2+GvCyXgkCqer0jceybYgTmNq7CoB8+dwf2xAG5L3ErLTmb2zj6pPatj3cgaNnjgfKrQDQMZdMLxs5ZAmnNqOCPkU/yR8uVLZcEoraJ9IDySGjyWgGdWvH5qME+tCWvoHpToG9ZNZJWnMz2FNfdWCNTxaaipBOCSKVMBHtEx1LZE5BJi5T5vddq5auzjg==~1; adblocked=true; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1665976089000@firstcreate:1602138027142"; xptwg=1807693626:EF199E6B4F2190:268695F:8512670C:560B14D5:2008F7D1:; xpm=0%2B1665976096%2BfkwE8VRmVw-3LPBUvNgfxM~%2B0; TS012768cf=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS01a90220=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS2a5e0c5c027=08fe679738ab20003e547791d391c11d03543faee317a34af73683f67d11bed0848ec9958b14d7be08ff158dde113000b92c659176ce76552d84422c2a3dc706b2dd6b26d2ed9fe03e5891888290f521341f2b9b7adf124911b55cf35a3762fe; bm_sv=9861D1A104E457F58104513D27C61FE0~YAAQDVLIF7Gg0diDAQAAxNjp4xFoSf1OCys7PILizMWHyEhzaW/6hGQcKK51nDrysHZIHOqa7w8pMZpHlrj7hN3qUTBZFo2TUIHjR2iN62eXJFt9n4RkRXZFz+vxocm5hwQjUeUIgTqD97wif+mioH3dN5SArS20LJkycP+fJgZSVThgBK24P13Uyf4itjYQLFoic3INDjvjtDnreBngGXpr7UkcxmKktKfXXvOzhsdjExUOAX+U0cMlB2UKbVptdrQ=~1; ACID=79be637b-6d55-4198-bc7f-702c3e95f2fa; TS01a90220=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; hasACID=true; vtc=b5jNbO62qAh0b8YyVrRJ60; xptwg=1318782031:114459438E84300:2C870B8:98A8505:E75DA1FB:7A8C437A:; xptwj=cq:7bfe79cbb34b6ed83ad2:J0SmeuIggQVJ2hFqVjB+hq7CNSP895d1DIF4pCwRVhQ9tk8BsiPCN/dmdBrxDFWN7e4CKH4boZWdZ+m9z+qpCYzIs2B02zsIFaBTh1xPx83NcDKmDUcpnFrhsabUEE4=; TS012768cf=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; _pxhd=18a50fcfff40c3bebcd2538552476ffb06ba17552884265c365a7cdb84f5f040:cdb44efb-4991-11ed-84a5-7656696c4472; akavpau_p2=1665513209~id=ae7da43442a7ed36c30e32159d4a8d96',
        # 'device_profile_ref_id': 'Rygd3MFxnSho6KM-g8Dy0gVBmdTiP_SnnT8y',
        # 'referer': 'https://www.walmart.com/search?q=broccoli',
        # 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'traceparent': '00-ff829608b459efbcd79c70dc23d78aea-ccdee82fa114de4a-00',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        # 'wm_mp': 'true',
        # 'wm_page_url': 'https://www.walmart.com/search?q=broccoli',
        # 'wm_qos.correlation_id': 'LIT9_N4_rVONMsRogxX5DEnsoF_In1bmGXbs',
        # 'x-apollo-operation-name': 'Search',
        # 'x-enable-server-timing': '1',
        # 'x-latency-trace': '1',
        # 'x-o-bu': 'WALMART-US',
        # 'x-o-ccm': 'server',
        # 'x-o-correlation-id': 'LIT9_N4_rVONMsRogxX5DEnsoF_In1bmGXbs',
        # 'x-o-gql-query': 'query Search',
        # 'x-o-mart': 'B2C',
        # 'x-o-platform': 'rweb',
        # 'x-o-platform-version': 'main-1.25.0-b626c5',
        # 'x-o-segment': 'oaoh'
        # }

        url = "https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22broccoli%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22broccoli%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Afalse%2C%22pageType%22%3A%22SearchPage%22%7D"
        payload={}
        headers = {
        'authority': 'www.walmart.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'ACID=ab06e761-799b-44b1-8624-faf712b84719; hasACID=true; assortmentStoreId=2251; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=UGU5eVHk5EhK7aTJFJweZI; _pxhd=556a049578e9ec6fe972d07ab3ec59d1b2b8bcbb95c4e06b4a1c68d8067ed206:dc140c09-6a1b-11ed-8b11-795146435366; TBV=7; _pxvid=dc140c09-6a1b-11ed-8b11-795146435366; adblocked=false; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjkwOTAzNDA4MTJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2OTA5MDM0MDgxMiwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY5MDkwMzQwODEyLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YWIwNmU3NjEtNzk5Yi00NGIxLTg2MjQtZmFmNzEyYjg0NzE5In0%3D; bstc=Wfy0bnFT5zy32HEwTe_tvQ; mobileweb=0; xptc=assortmentStoreId%2B2251; xpth=x-o-mverified%2Bfalse; xpa=; _astc=68e12af5a2485f61a9640813d9494eb6; pxcts=c1f0dc84-6a96-11ed-80c9-74525754424e; ak_bmsc=77058B983DAD6743D2E4D1607840369E~000000000000000000000000000000~YAAQB1LIF+KnTpuEAQAAA96uoBFVGTTDpJymd9wnhNucUQmeUSKlcG+GwPDJ2vjM+qFgjyjFynYGWU2CoZ3X2CnzUie5CrKpBUAEHiXpHaq/SpXPCPqF6r6H4iTADN3JbeH7UgVfhzIc2hkeS4CeRMcWq1gunqIk9CGnazlPgoXnrBsBVGixzJG9mGjLQv8uKxXE8pD2TbGAH6jhzCGcwXkIKwXTMTXa++nB3m97slBeFFUSBLTo15C72h4QC8Qm6xugLMacInftlMT4KltE7RQfOSXo33U9BE0m+rT29hhhlCXYhz89Ff8/iUOB2Lox1sB09aisYTjyUocTyPcBnuOv5b7pPl8eCyjEasqNyl0GfE+IPxKTcvqF1DFooZaF+xtbxjyZR0aiouoUAxDfhHtHqML1ZuBO/M4jH4SFUbabffQiLTae/zPGfBdbfml5aNnUIzT4yfPWIBkPqSPeUTmXGrT39azyF1uZcPTb4VarlJt3F/3r9glpt6Q=; wmlh=3b89c21b51eb8b365a33b532b20b3382a324d50a4d223fc09a93049c8acbe5cd; auth=MTAyOTYyMDE4Bak0%2ByYscDMh4nQihmaXma8tXP4Vh%2B65qFLv03AVr6fjsGOjMpVBt8vWmG7OTgZqZj405hB6kClT3mK8dXIR52zZ0XpW3m6Yw%2Fkb6WuvtY3ZNOG1r7BXBpEGcSn6kmks767wuZloTfhm7Wk2KcjygpySosImygUk1x1iKsdnk4%2BWTUBZJtScnjnyj6cO0BdyG7ZNY0bc90Q1Z%2F3liWmXdfgBIoW0QgNRTL3xG26qc1oUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrv5mz2%2FxGat%2BZvkzM5Z0PZ7AR2I8FUW05aBU8JoaK6D%2BN%2BtZ%2FlhOXSR7SRr7r1q94ym48kwO6iO63RwUR0zNXxdp65lGn5jb83oPP10O2tO1RuiPGH0mbdHq9XwQsE17KhAbajmc3a6HQbHZlS9HWyI%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTE2NzcxNzg3OCwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmFiMDZlNzYxLTc5OWItNDRiMS04NjI0LWZhZjcxMmI4NDcxOSJ9; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222254417983729%3Alastupd%3D1669147575213; xptwj=rq:ee35cdcc7e82e0c55b16:CgFls4YXhbNl7aEgKWUwyJVK/YY24e3PH3mrMN1d8e04K1bVqZOwMUwPHkZ/Ani987VkEGlvopXA/pJuDw/jS0bQhT3O5Vd6b2W4j3ocHyOh/Xc7x36fsfUbsL0zBs4WrDdJD74pvrzqFQ+wqULSWo4=; akavpau_p2=1669148175~id=d62e405f467620ad6a66e4d5f1842422; dimensionData=754; _pxff_cfp=1; com.wm.reflector="reflectorid:22222222254417983729@lastupd:1669147576000@firstcreate:1669147575213"; _px3=2fd661b00c31b0aa82683619ecabb2ef33a3823fd9a35d42209eaee8aa1f7891:qgnXmf3+wdo71HYEzSNw8cUvXJ3fegEkM5JaPQOJzr71Rn+NFFSPVCyC5QP3zQtu6QRVkkLZc3zRM1QLKu30rA==:1000:wtzGb/99ept/8eyHv9Gct32ASAadUXSH2LzM+7IaYeorsKr/Pd9eUhbNKsUfBRAVB5AQnz3w6e4xtSdNRY64/Fa0bdXwQBCnl8HL+WAymUIejXkdLSJT/fN3ob7h780/SokByA0VOYPzw5fc6NsUCUzq4lvAqYCG0iFJbjDjEBErMtvq5tTzq2ajGWp0eOG+OyWNGlovtGJTm6nXhGfMgA==; xptwg=3879158563:B9BEA7F3469380:1DDF2FA:D288B67B:61F65D39:E96DEA43:; TS012768cf=018cf40c2cd9433a6fac73c6c772129d569064457597348b893a4569872d81ec62a295443265e82271aa8099a86a84d184e06ddce2; TS01a90220=018cf40c2cd9433a6fac73c6c772129d569064457597348b893a4569872d81ec62a295443265e82271aa8099a86a84d184e06ddce2; xpm=3%2B1669147589%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; TS2a5e0c5c027=087b34fe23ab20002e92817d434d5cca0132432818e7412ba06262a4ad1aac75270423b083b54c4208585d82cb1130007ade91f79a2eeabda803aa687a8152c97dec537556b2f249fa7154d5a647f5a647d7d9d3da5fec53694d568a1bd80f52; bm_sv=987C6D61907ADD78F157C9AD177E86F0~YAAQB1LIFx+PVpuEAQAAb/zyoBFwdMwG6CBJl9MOpyC3uBhzrBOvFTU4D4BOg5guxJlXktvwTp/HC/5zM9yOklLfgTldJTnHsP7ZTJAQz46oeOi752kF+vwiYd/ArSJPoNAie9/QNeS5v0NzNTN/90vpoOrgT+1DJzE2hq+QeGUww+tmI2cswxTWRizx8Sb0N/6R+sEb1yp14LyWZqQAlZb3bKp+MLwZKY072GcOg84H2pWoR07EwF/3EHTli493ZG8=~1; ACID=547d8d74-bddd-49c4-a124-831b6c6d20f8; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS01a90220=019b75483df5ad845f3a0f54f137e5da1569c71cdfa8e270085893d59435f8050d696ff2526c9ccb73ba446186950b69c085ee0722; assortmentStoreId=2251; bm_sv=987C6D61907ADD78F157C9AD177E86F0~YAAQBlLIFwYh26CEAQAAJjj7oBEkZ7FexGIMn7gMDJPA5f2ybJh7Qe6rxZ8JxXRDH3FBOYsR7HDuY+t/0X7JkAmnVRr9wshYMRPn47fiWBfyqWZ1f0LLSPZ3yNsUEqdkCCCijohZva+1qW/EfedbNJgScuKAlCoyK09IUtsD5bAYywgNMkyJncIkZRShpNZ2ocG8F0peI024eet6xrikvrjLvwuQCDB9Sl2eAfiFJc3199ICIUlHdGHbVYQtWRLSA20=~1; bstc=Wfy0bnFT5zy32HEwTe_tvQ; com.wm.reflector="reflectorid:22222222254417983729@lastupd:1669148129000@firstcreate:1669147575213"; hasACID=true; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0JBS0VSWSIsIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9TUEVDSUFMX0VWRU5UIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTExNDA0ODg3MSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjU0N2Q4ZDc0LWJkZGQtNDljNC1hMTI0LTgzMWI2YzZkMjBmOCJ9; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMjI1MSIsInRpbWVzdGFtcCI6MTY2OTA5MjQ0ODg2OH0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjY5MDkyNDQ4ODY4LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTE3NDQiLCJjaXR5IjoiTGEgUHVlbnRlIiwic3RhdGUiOiJDQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyMjUxIiwidHlwZSI6IkRFTElWRVJZIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2NjkwOTI0NDg4NjgsImJhc2UiOiI5MTc0NCJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo1NDdkOGQ3NC1iZGRkLTQ5YzQtYTEyNC04MzFiNmM2ZDIwZjgifQ%3D%3D; mobileweb=0; vtc=UGU5eVHk5EhK7aTJFJweZI; xpa=; xpm=3%2B1669148128%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; xptc=assortmentStoreId%2B2251; xpth=x-o-mverified%2Bfalse; xptwg=248156628:1FEBD1385B08140:52234E4:151DE32C:6C7C2091:92263C79:; xptwj=rq:56555ca0cecaad9a50da:oGFGwCY0K2WeLbtwhQuqfsPe8yki4ZhEwcJwHcNYB2sF3nCe6Sr/uor4JosU6YvG0L24SPxlS2zq8vV/b/hWsi2CoOG01oSuo5ALMdytOPNkgY2M2MpsJhM=; TS012768cf=019b75483df5ad845f3a0f54f137e5da1569c71cdfa8e270085893d59435f8050d696ff2526c9ccb73ba446186950b69c085ee0722; TS2a5e0c5c027=08013b6833ab2000212165bf28ec6de33bb70fd19c56a65466d1a589ffe859a78faa282cd4daa0d60805c3a70a1130003f8c0979ba1925403599315d49ee183de0832847477af77d72338bfa35714f867ea6d236c16323981ba15c81520356e0; _pxhd=677d0fc014d912fd62a2e7ee1192793c80bee74fc7f09625e15facdfb821f97c:c490d453-6a20-11ed-a3e9-54766f4c5843; akavpau_p2=1669148729~id=1f15f8bdd65626e4d4d687a99c9a0eb3',
        'device_profile_ref_id': 'cvqfZESMkKoPV9cVCESMqeoeHrr6UZGZoDPT',
        'referer': 'https://www.walmart.com/search?q=broccoli&typeahead=broc',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-b3780c005ea59f17c9e094e454a1cc56-d61a2e0f58391370-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'wm_mp': 'true',
        'wm_page_url': 'https://www.walmart.com/search?q=broccoli&typeahead=broc',
        'wm_qos.correlation_id': 'lyqiu2y49CVbahAGwk0PkLRWrlM97RN9iFuU',
        'x-apollo-operation-name': 'Search',
        'x-enable-server-timing': '1',
        'x-latency-trace': '1',
        'x-o-bu': 'WALMART-US',
        'x-o-ccm': 'server',
        'x-o-correlation-id': 'lyqiu2y49CVbahAGwk0PkLRWrlM97RN9iFuU',
        'x-o-gql-query': 'query Search',
        'x-o-mart': 'B2C',
        'x-o-platform': 'rweb',
        'x-o-platform-version': 'main-1.32.0-b2719e',
        'x-o-segment': 'oaoh'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        searchedItems = json.loads(response.text)
        print(searchedItems)

        # itemID = {}
        # itemInfo = {}

        # for num,i in enumerate(searchedItems['data']['search']['products']):
        #     itemID[num] = i['item']['product_description']['title']
        #     itemInfo[i['item']['product_description']['title']] = {'price' : i['price']['formatted_current_price'],
        #                                                             'rating' : i['ratings_and_reviews']['statistics']['rating']['average'],
        #                                                             'imageURL': i['item']['enrichment']['images'],
        #                                                             'buyURL': i['item']['enrichment']['buy_url'],
        #                                                             'description' : i['item']['product_description']['soft_bullets']['bullets'],
        #                                                             'allergies' : i['item']['product_description']['bullet_descriptions']}

        # print(itemID)
        # for i in itemInfo:
        #     print(i,'\n',itemInfo[i],'\n\n')
        # items = [itemID,itemInfo]
        # return items[itemID,itemInfo]
    def targetItems(self,itemSearch,storeID):

        url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword=ice+cream&offset=0&page=%2Fs%2Fice+cream&platform=desktop&pricing_store_id=1028&scheduled_delivery_store_id=2147&store_ids=1028%2C2147%2C1033%2C222%2C767&useragent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F106.0.0.0+Safari%2F537.36&visitor_id=0183A19D5C1D0201BE60A72076D3873E&zip=91792"

        payload={}
        headers = {
        'authority': 'redsky.target.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'TealeafAkaSid=zQiS7YFzDuDmwVo2bHjNJ6KfGQfSYjGQ; visitorId=0183A19D5C1D0201BE60A72076D3873E; sapphire=1; UserLocation=91792|34.020|-117.900|CA|US; ci_pixmgr=other; crl8.fpcuid=1e3c6df0-d017-4c02-98b8-3171eed4203c; fiatsCookie=DSI_1028|DSN_West%20Covina|DSZ_91791; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI5NDkzMDRiNC1jOGQ1LTQyY2YtOWUwMC01NzQ5OTU5OTRiMzIiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjYwNjE5NDgsImlhdCI6MTY2NTk3NTU0OCwianRpIjoiVEdULmM5NjA4ZjYxOTVlYTRiMzRiMWJhZGI1OWZjZDg1NDIwLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImNhYWJhYTlkNmRhY2Q0MTkyZTZmMzRjN2FhMWNiMjNhZTY3ZmE2ZjhhYjc5MzcxYWUyNGQwYjk4YWVhMTkyMmEiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.SqRPiwH2zBMxLpDt_zK6bp5DgNagz4Fg68QsjGjN5oaGAHX_9yxnpyl-6J7U0jzO-ilv2P_A234Hu2Ys3uiCIYY2jbxqyUseG5rPc4l4rMaLeFBqU4Kp7LUsgI_QPuGHlpWshRL-axxwy1I9Uu3KUY80MDS2B_lj5lzESVNOgJJOJUCTNJgip2x1bFvJZogad0mecRHEaJuTcaZ1W8BrbUQTpb833u-uKUdYEwrR30eB-jd_5kJLWIozG4DSyyzBv_2UZYqldLqZl2TVu7gqnAMaLO6MCvYK_xoPSCvEtusY9OudlUQU4vA7RbMruyviixGNeb0rRz8iJ0FAwdIdHA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiI5NDkzMDRiNC1jOGQ1LTQyY2YtOWUwMC01NzQ5OTU5OTRiMzIiLCJpc3MiOiJNSTYiLCJleHAiOjE2NjYwNjE5NDgsImlhdCI6MTY2NTk3NTU0OCwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlfX0.; refreshToken=qjvkF1sANHoiVenSt6xK7yFZrRHmYbQOSk4GgQ317kzSwOr0dRbh40YKvv4OzVAC04KOAoBDXR4eDCQeelu75Q; _mitata=MzAzMmM5YjYyMmIzMzRjZTdmM2E5N2M3YmIxNGEyY2FiMzZmMmM2NWUzZTQxZTJhZTE5MWNkNGYzYmIzZmE3Yg==_/@#/1666039438_/@#/c1iy9LrBn53DJEiz_/@#/ZGIzNDE5N2FiYzM1NmVmODgyNjU3NWM4NDlkYjRhZDM2YTA1OTcyNjRlM2ZmZDg2MTE2NjYyYjc5NTViYmFkNw==_/@#/000; ffsession={%22sessionHash%22:%221fd7f4fa462a241665710136187%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=ice+cream%22%2C%22prevSearchTerm%22:%22ice%20cream%22%2C%22sessionHit%22:22}',
        'origin': 'https://www.target.com',
        'referer': 'https://www.target.com/s?searchTerm=ice+cream',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        searchedItems = json.loads(response.text)

        itemID = {}
        itemInfo = {}

        for num,i in enumerate(searchedItems['data']['search']['products']):
            itemID[num] = i['item']['product_description']['title']
            itemInfo[i['item']['product_description']['title']] = {'price' : i['price']['formatted_current_price'],
                                                                    'rating' : i['ratings_and_reviews']['statistics']['rating']['average'],
                                                                    'imageURL': i['item']['enrichment']['images'],
                                                                    'buyURL': i['item']['enrichment']['buy_url'],
                                                                    'description' : i['item']['product_description']['soft_bullets']['bullets'],
                                                                    'allergies' : i['item']['product_description']['bullet_descriptions']}

        print(itemID)
        for i in itemInfo:
            print(i,'\n',itemInfo[i],'\n\n')
        items = [itemID,itemInfo]
        return items[itemID,itemInfo]
            
def getWalmartPrices(walmartItems):
    print("hi")
        # prices = []
        # for x in walmartItems[1]:   #Item Info
        #     #print ("Item: " + x)
        #     for y in walmartItems[1][x]:    #Keys of Item Info: shortDescription, imageURL, currentPrice
        #         if(y == "currentPrice"):
        #             #print (y,':',walmartItems[1][x][y])
        #             for key, value in walmartItems[1][x][y].items():   #Keys and values of currentPrice
        #                 #print("Key= " + key, " : Val= ", value)
        #                 if(key == "price"): #Append Int price to list
        #                     prices.append(value)
        #                     #print(value)    
         
        # prices.sort()   #Sort list of prices
        # return prices[0]


getitem = getItems()
walmartItems = getitem.walmartItems('broccoli', '3133')

cheapestWalmartPrice = getWalmartPrices(walmartItems)
print("Cheapest price found", cheapestWalmartPrice) 
