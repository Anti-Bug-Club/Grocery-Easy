from re import I
import requests
import json

class getItems():
    def walmartItems(self,itemSearch,storeID):
        # url = f"https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22{itemSearch}%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22broccoli%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Atrue%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Atrue%2C%22pageType%22%3A%22SearchPage%22%7D"

        # payload={}
        # headers = {
        # 'authority': 'www.walmart.com',
        # 'accept': 'application/json',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'content-type': 'application/json',
        # 'cookie': f'vtc=fkwE8VRmVw-3LPBUvNgfxM; _abck=j4ghcbkkk1iuv5qb24hx_1862; ACID=6783deab-9a62-4b24-a4d5-e588fdc0666b; hasACID=true; _pxhd=316d5c7455b27df562b67b440944523aebc9a7401d75e01330feb78c4f1dd7f8:8851bd59-43aa-11ed-9e97-494754667142; TBV=7; dimensionData=939; pxcts=a2f5ad62-4b37-11ed-ad0c-564b7a737341; _pxvid=8851bd59-43aa-11ed-9e97-494754667142; auth=MTAyOTYyMDE4iiKp5NrTopjDlrUwU1z2tcONrNYiFumPS1UYpvtiyqxs%2BKC8RG4J8bntpo5jdqSF%2BgQVe0rrArzHa77vlpyLSjWOtx9gkmiYZiKnGbvhKowQcmRi6ZK3UHmFbLMwrc0w767wuZloTfhm7Wk2KcjygkeeSCv4Chv5IarMOQ7pqjdWfTH9BATfrnclOUjuedDm0o70w6NgikYOn3qtcJgcTGK0H82ifhi7ivFxwLwbe3gUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrm5%2BH7OFk5snY5qeMwazalZrKyvt84Os4oqUXIb427dEzKyJRIFmY9DiRybhtLpH0KPjHt0LFJA8yk74a1ppaaY4idXL%2BRf7%2FlyNWwZnxBX2nG3Rj7sHAaWfI2DqvK1c7JE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJQSUNLVVAiLCJwaWNrdXAiOlt7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiMjI1MSIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdfV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzQuMDMwNCwibG9uZ2l0dWRlIjotMTE3Ljk0MDMsInBvc3RhbENvZGUiOiI5MTc0NCIsImNpdHkiOiJMYSBQdWVudGUiLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjIyNTEiLCJkaXNwbGF5TmFtZSI6IkNpdHkgT2YgSW5kdXN0cnkgU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5MTc0NSIsImFkZHJlc3NMaW5lMSI6IjE3MTUwIEdhbGUgQXZlIiwiY2l0eSI6IkNpdHkgT2YgSW5kdXN0cnkiLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5MTc0NS0xODA5In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozMy45OTg0MzcsImxvbmdpdHVkZSI6LTExNy45MzIzNzZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic3RvcmVGZWVUaWVyIjoiQiIsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMjI1MSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NjU5OTY4NDcyMjMsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo2NzgzZGVhYi05YTYyLTRiMjQtYTRkNS1lNTg4ZmRjMDY2NmIifQ%3D%3D; assortmentStoreId={storeID}; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJQSUNLVVAiLCJpc0V4cGxpY2l0IjpmYWxzZSwic3RvcmVJbnRlbnQiOiJQSUNLVVAiLCJtZXJnZUZsYWciOnRydWUsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjQ4NjM2OTExMzN9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2NTk3NTI0NzIyMSwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY0ODYzNjkxMTMzLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6Njc4M2RlYWItOWE2Mi00YjI0LWE0ZDUtZTU4OGZkYzA2NjZiIn0%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; bstc=ZDrBxYKn779_q4prevlq74; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=1W06O|1ymNb|20yr2|3mpU4|5_9FA|5f4tU|9CVUZ|CQWzm|C_vdV|DJvKV|GzUv6|H9VcM|HUnA1|HjWUQ|JCPlz|JnuDC|NBAls|OH8Y5|Qz3xl|Rgq78|Rt7EL|SPL_W|SmVSa|V9eZu|XA_S7|c6tgM|c8HYq|g0dgr|hYHrN|o7VCR|opFAJ|pSCez|qb-IF|rlJqf|rtb_E|s4Kzt|sQWPT|tyeB4|tzVuW|u8ztl|udhq9|vCU7g|vTmRC|wPXtX|xI7yg|xOe2Z|xdwD5|xlLfn|y-oun; exp-ck=1ymNb320yr213mpU415_9FA2CQWzm1DJvKV1HUnA11HjWUQ1JnuDC1NBAls1Qz3xl1Rgq781Rt7EL2SmVSa1XA_S71c6tgM3c8HYq1g0dgr2opFAJ1pSCez1qb-IF3rtb_E1s4Kzt1tyeB41u8ztl1udhq91vCU7g1vTmRC1wPXtX2xdwD51y-oun1; xpkdw=1; ak_bmsc=9C9C28808354ACB980C085C3E72FEB59~000000000000000000000000000000~YAAQDVLIF75K0NiDAQAAruTc4xGwPMsDiOja0KEYWBlXqy8V7wqbw4U9As4144kYhw6MVssD/uJBi+k7A87WBlW6cxWemyl46GFQvAWVHdKRzsgxnQdF//fdtj/YNH55ZLwZxooiE2c1FF7e2wvUVrBc7xhWZpQm28ZElmrRHb76L0UJndPLGKvIQnUb9EqkMoxgI2puOHKUwXDQ+ymOhtvsUu5A08pWS9zHABC9EOERgaL/BrRs7h8vCJGTdzCHqah+q8JIngw1cdt4pKCxcxNF/Y0/DeIpbvlFwmBBaenrto9rWHBV/KEcLsCuv9VRM1jWX0zohUpJXDEResaP8dJT2qBv5N/jL3lcHZA6cotVXCH3jjctzBRVZMdFf2BIMnFIy16kKvKj8bbzv8T+DTyI8mNdi3/FEK135ttV0c+kmTGlPz2xz0WCnZwzav2yZj3T0qw1u+fen5bjjmnkvy3XWP6e4wWT9u9vIf3IXJ0=; _astc=000b0131101bd57b85394ceaac8b5797; xptc=assortmentStoreId%2B{storeID}; xptwj=cq:cc86724c1cbc0fd0e545:PgsGWdiknO/KdOfrICWBO0DQj4YT3A0totIubb6M5eulnwCFN8NacXNZjlbfwVWYALwx74liD7Gdf9lTurQ5w3cu1yP5l86HG9D25vADGku2CzOj5NWYFL4DPiwGEvVzpbGu3LTlgfMiy/vn1kCYXnqRYJI=; akavpau_p2=1665975853~id=e10b5c4546fc2009a2e0de259668ac30; bm_mi=49C2D0B5BE317A0682E4AD3C053FA044~YAAQDVLIF5ZM0NiDAQAAY/jc4xFzYFqXZzmhPOWSQyBk4bTTOhg5F2SqVHMam0KWhJhTSQnDSM2zwCd78NChgJRieXSWvc5win3j7+G+2DD4cu+fZXRv9Y6sknEfCrEC9qqd+/9FmaDQyVNSCAhCie9kcX77U/jDqr56h2+GvCyXgkCqer0jceybYgTmNq7CoB8+dwf2xAG5L3ErLTmb2zj6pPatj3cgaNnjgfKrQDQMZdMLxs5ZAmnNqOCPkU/yR8uVLZcEoraJ9IDySGjyWgGdWvH5qME+tCWvoHpToG9ZNZJWnMz2FNfdWCNTxaaipBOCSKVMBHtEx1LZE5BJi5T5vddq5auzjg==~1; adblocked=true; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1665976089000@firstcreate:1602138027142"; xptwg=1807693626:EF199E6B4F2190:268695F:8512670C:560B14D5:2008F7D1:; xpm=0%2B1665976096%2BfkwE8VRmVw-3LPBUvNgfxM~%2B0; TS012768cf=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS01a90220=01d9f1a181dfc1d33ada0a5dd20429885d2dca4f5f4b3da8983168f86d8aff6f406b2c782e8e9aadab1e1ba0994521d884bcba3a2e; TS2a5e0c5c027=08fe679738ab20003e547791d391c11d03543faee317a34af73683f67d11bed0848ec9958b14d7be08ff158dde113000b92c659176ce76552d84422c2a3dc706b2dd6b26d2ed9fe03e5891888290f521341f2b9b7adf124911b55cf35a3762fe; bm_sv=9861D1A104E457F58104513D27C61FE0~YAAQDVLIF7Gg0diDAQAAxNjp4xFoSf1OCys7PILizMWHyEhzaW/6hGQcKK51nDrysHZIHOqa7w8pMZpHlrj7hN3qUTBZFo2TUIHjR2iN62eXJFt9n4RkRXZFz+vxocm5hwQjUeUIgTqD97wif+mioH3dN5SArS20LJkycP+fJgZSVThgBK24P13Uyf4itjYQLFoic3INDjvjtDnreBngGXpr7UkcxmKktKfXXvOzhsdjExUOAX+U0cMlB2UKbVptdrQ=~1; ACID=79be637b-6d55-4198-bc7f-702c3e95f2fa; TS01a90220=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; hasACID=true; vtc=b5jNbO62qAh0b8YyVrRJ60; xptwg=1318782031:114459438E84300:2C870B8:98A8505:E75DA1FB:7A8C437A:; xptwj=cq:7bfe79cbb34b6ed83ad2:J0SmeuIggQVJ2hFqVjB+hq7CNSP895d1DIF4pCwRVhQ9tk8BsiPCN/dmdBrxDFWN7e4CKH4boZWdZ+m9z+qpCYzIs2B02zsIFaBTh1xPx83NcDKmDUcpnFrhsabUEE4=; TS012768cf=01aed3d184bd9d5ca8ee11a4ca5e910dbd9d1a95906a39bd2dd3953ae17a29d231520997f50c0bd842cecf459e893db2a958b3d327; _pxhd=18a50fcfff40c3bebcd2538552476ffb06ba17552884265c365a7cdb84f5f040:cdb44efb-4991-11ed-84a5-7656696c4472; akavpau_p2=1665513209~id=ae7da43442a7ed36c30e32159d4a8d96',
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

        url = "https://www.walmart.com/orchestra/home/graphql"

        payload = json.dumps({
        "query": "query AdV2( $platform:Platform! $pageId:String! $pageType:PageType! $tenant:String! $moduleType:ModuleType! $pageContext:PageContextIn $locationContext:LocationContextIn $moduleConfigs:JSON $adsContext:AdsContextIn $adRequestComposite:AdRequestCompositeIn ){adV2( platform:$platform pageId:$pageId pageType:$pageType tenant:$tenant moduleType:$moduleType locationContext:$locationContext pageContext:$pageContext moduleConfigs:$moduleConfigs adsContext:$adsContext adRequestComposite:$adRequestComposite ){status adContent{type data{__typename...AdDataDisplayAdFragment __typename...AdDataSponsoredProductsFragment __typename...AdDataSponsoredVideoFragment}}}}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment AdDataSponsoredProductsFragment on AdData{...on SponsoredProducts{adUuid adExpInfo moduleInfo products{...ProductFragment}}}fragment ProductFragment on Product{usItemId offerId badges{flags{__typename...on BaseBadge{id text key query type}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought criteria{name value}}}labels{__typename...on BaseBadge{id text key}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{id text key}}}priceInfo{priceDisplayCodes{rollback reducedPrice eligibleForAssociateDiscount clearance strikethrough submapType priceDisplayCondition unitOfMeasure pricePerUnitUom}currentPrice{price priceString priceDisplay}wasPrice{price priceString}priceRange{minPrice maxPrice priceString}unitPrice{price priceString}savingsAmount{priceString}comparisonPrice{priceString}}showOptions sponsoredProduct{spQs clickBeacon spTags}canonicalUrl numberOfReviews averageRating availabilityStatus imageInfo{thumbnailUrl allImages{id url}}name fulfillmentBadge classType type showAtc p13nData{predictedQuantity flags{PREVIOUSLY_PURCHASED{text}CUSTOMERS_PICK{text}}labels{PREVIOUSLY_PURCHASED{text}CUSTOMERS_PICK{text}}}brand}fragment AdDataSponsoredVideoFragment on AdData{...on SponsoredVideos{adUuid adExpInfo moduleInfo videos{video{vastXml thumbnail spqs}products{...ProductFragment}}}}",
        "variables": {
            "adRequestComposite": {},
            "adsContext": {
            "locationContext": {
                "zipCode": "91744",
                "stateCode": "CA",
                "storeId": "2251",
                "pickupStore": "2251",
                "deliveryStore": "2251",
                "intent": "SHIPPING",
                "incatchment": True
            },
            "itemId": "51259307",
            "categoryId": "976759_976793_8910423_4023809",
            "categoryName": "Food/Fresh Produce/Fresh Vegetables/Broccoli & Cauliflower",
            "brand": "PRODUCE UNBRANDED",
            "productName": "Broccoli Bunch, Each",
            "productTypeId": "208",
            "normKeyword": "",
            "verticalId": "",
            "dedupeList": []
            },
            "pageContext": {
            "itemContext": {
                "itemId": "51259307",
                "categoryPath": "0:976759:976793:8910423:4023809",
                "categoryPathName": "Home Page/Food/Fresh Produce/Fresh Vegetables/Broccoli & Cauliflower",
                "name": "Broccoli Bunch, Each",
                "brand": "PRODUCE UNBRANDED",
                "partTypeID": "",
                "manufactureNumber": "0",
                "aaiaBrand": "",
                "tireSize": "",
                "tireWidth": "",
                "tireRatio": "",
                "tireDiameter": "",
                "wheelDiameter": "",
                "speedRating": "",
                "loadIndex": "",
                "viscosity": "",
                "type": "REGULAR",
                "productTypeId": "208"
            }
            },
            "pageId": "51259307",
            "pageType": "ITEM",
            "platform": "DESKTOP",
            "tenant": "WM_GLASS",
            "locationContext": {
            "storeId": "2251",
            "stateCode": "CA",
            "zipCode": "91744"
            },
            "moduleConfigs": {
            "moduleLocation": "bottom",
            "lazy": "1200"
            },
            "moduleType": "SponsoredProductCarousel"
        }
        })
        headers = {
        'authority': 'www.walmart.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'ACID=ab06e761-799b-44b1-8624-faf712b84719; hasACID=true; assortmentStoreId=2251; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=UGU5eVHk5EhK7aTJFJweZI; _pxhd=556a049578e9ec6fe972d07ab3ec59d1b2b8bcbb95c4e06b4a1c68d8067ed206:dc140c09-6a1b-11ed-8b11-795146435366; TBV=7; pxcts=dcb488ae-6a1b-11ed-9c6b-447759514353; _pxvid=dc140c09-6a1b-11ed-8b11-795146435366; _astc=68e12af5a2485f61a9640813d9494eb6; adblocked=false; wmlh=3b89c21b51eb8b365a33b532b20b3382a324d50a4d223fc09a93049c8acbe5cd; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjkwOTAzNDA4MTJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2OTA5MDM0MDgxMiwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY5MDkwMzQwODEyLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YWIwNmU3NjEtNzk5Yi00NGIxLTg2MjQtZmFmNzEyYjg0NzE5In0%3D; auth=MTAyOTYyMDE4Bak0%2ByYscDMh4nQihmaXma8tXP4Vh%2B65qFLv03AVr6fjsGOjMpVBt8vWmG7OTgZqZj405hB6kClT3mK8dXIR52zZ0XpW3m6Yw%2Fkb6WuvtY3ZNOG1r7BXBpEGcSn6kmks767wuZloTfhm7Wk2Kcjygv3M5Jnvc7ePkiG6%2BkglNADS2XTJUwMm6dnIM4w0x6307e68ZyZLOT7mXakVgVgPTNB4urwS0PeT7Sq%2BHW7i1iYUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrpGWA3F36bUYcuAUrmA6PClEaEj%2BFZRs1wfVGuoIo0cBzehitFrS8KWErN6NY2aSC6xu%2BctlDLcuWGhgyNWyGpPa%2FHc6z%2BCyk%2FgMJtS0mqL7Fs0%2BsW0JeJqz1NJ8ZpRSzJE5WBBdZBCyKnCQAR7o6eg%3D; bstc=dS3m50_4xoQfphKutIkfsY; mobileweb=0; xptc=assortmentStoreId%2B2251; xpth=x-o-mverified%2Bfalse; xpa=; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTExOTIyMjUxNCwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmFiMDZlNzYxLTc5OWItNDRiMS04NjI0LWZhZjcxMmI4NDcxOSJ9; ak_bmsc=A9F8B8E7AEB0AA20FFE0C476542A5F31~000000000000000000000000000000~YAAQEVLIF7bCWoiEAQAAsIz4nRGNwL95/aFFgsCR48RLlOKZfExG9Jxam4VtBL2rdBib/ZOCJ/l+pgWWnyDQijwynCLbWBKZEdzGm2Oluas7pU1F8TDEcWsnHlW6MX29b+n9mobiebaihlubHyZ9CwA2tZKDxysr9nS0/GDOM1FBYk/ztbK8wF/1ZmyEUYipSV3h5nSogWR5AdeTbrAHQ83Icy356Bj3PlJUshDF10hEryTpa1jP8LEjmTv/RLcUi44f5pJ7q5V91O+zv19u6sjqZTh/KnP/E/XAzGQb6Pjk6CsVXf5ufyFjB4yzS2+2cRyELDLN7kgCdFdrMXcdLzE+h4N7kupsA8H4grqZ5OZdQ2T3UrnpmNgqcJV6sOmmJa9GOBmohYOFNAkHKP4jzm6RKiiKMDCfAbSzHaVCCcdYpBL2lCIz35OodNB9Jf4jGe53APYEr5XHq4WvpImQ1oLGuD3Y3/r1mA6zX34PQY/SGc9wpBvBKe/uIMA=; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1669097729666; __cf_bm=cRVoIJAWEI.YnKY30V_QN.1eJmjKzeMHSvdFw6YyB6I-1669097836-0-ARmoGZhLMJOlFvZg2dLkrMbWzdXvxXAr7vBoAaQJvOTJUVIHlKvFyKTHvPL0YCPNcEGBt8LRF4TvDbIj0lgko2Op3fVjPw8ZQArp0EnqSuBd; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1669098065852@firstcreate:1669090340769"; xpm=3%2B1669098065%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; xptwg=3930009485:BE6175F872AEF0:1E9E486:BC439D17:495BE5BD:1E9C6E38:; xptwj=rq:b207cb16a644a4aca4f8:Wfxkr+3QoZyVknPsPU6vpYlWVmTggUZcLT6trLkIwYCNHWNr1H5ogQ733GiVZrulZyzOBnE5NvUSY4voi5LV6VzrwMMJ8s/KdiqDsoE401sOWIU8K8qOhw3q1oDV4bLQTWsvGl0=; TS012768cf=01e94df8da1e351744c3d719b67fa38f70d28bb864f333a518fa9a9b5d1ed0074c9d8aa8bc43edf466d5ed3b4195c12ecb1819dba6; TS01a90220=01e94df8da1e351744c3d719b67fa38f70d28bb864f333a518fa9a9b5d1ed0074c9d8aa8bc43edf466d5ed3b4195c12ecb1819dba6; TS2a5e0c5c027=08fa7a0f15ab2000abe6214c3a9fced220985eedfcfc483f6f4f431aeab26e6d6681a89aa3d217f40899fd0107113000490ebd541443dcdeec7b33aa1b4cef1acbe0baa155fa224ab75ef2370d887c1ae9b858cdeeadf263f8af261fb62a1657; akavpau_p2=1669098666~id=5db143121fc027a8b60e39b7d8edf19e; bm_sv=2DDE726C530B97CDA92F6A1D898F2D5E~YAAQB1LIF5rmx5qEAQAA1lD/nREEDPJmkYpTRP5r5p1pI75vW2yyVJwuaD849DQ0UHagy3AM0MQcmctQoJoorPcI/SSnO45cDlFo9MsYkbWK7f6vTV+YK/zKr/lrytBeZV5gDMvniFDDtYa4baUbCRx7oaBLtBfoN0hTZzl7YlHyMJ5zNp4LfXCmbrO6L/ji1K0HK38B5Etmo1lSjkT3C/aoJZf5aLQc44DLauJ+n5APHJrqp6qFEE8b3vpqyYs2fQc=~1; ACID=547d8d74-bddd-49c4-a124-831b6c6d20f8; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS01a90220=01209de4728b1d50e8564676b30558c0cf189629e29f539e83046b6a9a977e5df24db8fc5eb3c946752619689dd8396b49c99395bf; ak_bmsc=844AB6585FD451FEFDFE4D5BD4495FC5~000000000000000000000000000000~YAAQB1LIF7EavpqEAQAAGJ6pnREmsqPzkqF7rOUHq8WKE/ExvvWzbqEXH6GY2K4qXy2dTB2LabLQdGTRtLPwLM5QqkgfkWmNKmj+s59Tv/E7/kJQ32qo+ix2ppwm/lVEtujsUUjplTQMZv+FpTL8AJpGioTyME7fIY+0Dis4ruALvtVFwIt7+Cdzwo2gVYodqnasZX+yNqItvQQxf48On0kXhGRkmD8UUueN7AX9yr37TTb1rvK3idd7g4M/99/Uf+yaivk8RPZ8nGJUn0+cBS1ihB8W7SAz04rS1V82BQElM8BYoRLEZxJ7rM8XltioCh6uM0s69cGb5tx615O2NIBDi2SDtkLGobQyKcm8ESuZ7+XUGt6k9QCeWDHF; assortmentStoreId=2251; bm_sv=2DDE726C530B97CDA92F6A1D898F2D5E~YAAQ1OnHF9Uwjo2EAQAAlDMBnhH1p+7vvO7M4BqNdWOE0Yi63utMg1KbTBkDAbi/jNoCJmtxYGQ9O8pHoCYYcXoEsj8dK26Jqr8ctGu8zsh/xg98PV1IZ2y/lVkICyl5yQV4Hlb57IUeCGBgVrAN0Sw81vG7sHhy3JHBqrWOhcvqCsVTWVCnAnxnUK5mOJHAOx4KBUqYxFajC2p3OIu/OpXVvkZBwSxJn6W0eB8mij06BrwIkh21QEfG1re08k7y78Q=~1; bstc=dS3m50_4xoQfphKutIkfsY; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1669098189000@firstcreate:1669090340769"; hasACID=true; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0JBS0VSWSIsIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9TUEVDSUFMX0VWRU5UIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTExNDA0ODg3MSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjU0N2Q4ZDc0LWJkZGQtNDljNC1hMTI0LTgzMWI2YzZkMjBmOCJ9; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMjI1MSIsInRpbWVzdGFtcCI6MTY2OTA5MjQ0ODg2OH0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjY5MDkyNDQ4ODY4LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTE3NDQiLCJjaXR5IjoiTGEgUHVlbnRlIiwic3RhdGUiOiJDQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyMjUxIiwidHlwZSI6IkRFTElWRVJZIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2NjkwOTI0NDg4NjgsImJhc2UiOiI5MTc0NCJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo1NDdkOGQ3NC1iZGRkLTQ5YzQtYTEyNC04MzFiNmM2ZDIwZjgifQ%3D%3D; mobileweb=0; vtc=UGU5eVHk5EhK7aTJFJweZI; xpa=; xpm=3%2B1669098189%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; xptc=assortmentStoreId%2B2251; xpth=x-o-mverified%2Bfalse; xptwg=3906994097:6E5DA9FDC0B408:11BFF12:EBE8F842:FE0D71AF:C184CE34:; xptwj=rq:d3c189dd452390d6b771:82fD8CjeNAwbm+BnNPiXLAVTcP1VFsyMsj4JI4QxObZ4xvdEFD6h7YlPqZCOHOjaAd7L/CtCldk//5Lf/DkpXBe9/wqW9fpYubOSk3VNstxjyMkIWFY=; TS012768cf=01209de4728b1d50e8564676b30558c0cf189629e29f539e83046b6a9a977e5df24db8fc5eb3c946752619689dd8396b49c99395bf; TS2a5e0c5c027=08e60dfdf6ab20006e80f38783ef6598a5cecd1865e74d2200013f1fc8aa5ee9bb1bbd766d22e93608feceee7e1130003d271fd5ce70df398faef7b64f01b0396c9b01e824785d53b8d4e8dbfbf1b19bc25bd2fed937e306b241c76bcbd9158b; _pxhd=677d0fc014d912fd62a2e7ee1192793c80bee74fc7f09625e15facdfb821f97c:c490d453-6a20-11ed-a3e9-54766f4c5843',
        'device_profile_ref_id': 'cvqfZESMkKoPV9cVCESMqeoeHrr6UZGZoDPT',
        'origin': 'https://www.walmart.com',
        'referer': 'https://www.walmart.com/ip/Broccoli-Bunch-Each/51259307',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-b9907e38c687c3bc58a8493e9ea5561f-d762f729dd85038a-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'wm_mp': 'true',
        'wm_page_url': 'https://www.walmart.com/ip/Broccoli-Bunch-Each/51259307',
        'wm_qos.correlation_id': 'uUe1Y-PIg7G6r8yOym_fv-C_sHznR7_jaUkH',
        'x-apollo-operation-name': 'AdV2',
        'x-enable-server-timing': '1',
        'x-latency-trace': '1',
        'x-o-bu': 'WALMART-US',
        'x-o-ccm': 'server',
        'x-o-correlation-id': 'uUe1Y-PIg7G6r8yOym_fv-C_sHznR7_jaUkH',
        'x-o-gql-query': 'query AdV2',
        'x-o-mart': 'B2C',
        'x-o-platform': 'rweb',
        'x-o-platform-version': 'main-1.32.0-b2719e',
        'x-o-segment': 'oaoh'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

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
