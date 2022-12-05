from re import I
import requests
import json


class getItems():
    def walmartItems(self,itemSearch,storeID): #add '%20' between words with spaces for itemSearch
        try:
            url = f"https://www.walmart.com/orchestra/snb/graphql/Search/0d430070b29087d0816fdde9b3007bc0d6142d39a2537d8a1fd02cb005ea23f8/search?variables=%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22{itemSearch}%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22{itemSearch}%22%2C%22page%22%3A1%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%22%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22broccoli%22%2C%22cat_id%22%3A%22%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%22%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22enableFacetCount%22%3Atrue%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchGallery%22%3Afalse%2C%22fetchSbaTop%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFlattenedFitment%22%3Afalse%2C%22pageType%22%3A%22SearchPage%22%7D"
            payload={}
            headers = {
            'authority': 'www.walmart.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': f'ACID=ab06e761-799b-44b1-8624-faf712b84719; hasACID=true; assortmentStoreId={storeID}; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=UGU5eVHk5EhK7aTJFJweZI; _pxhd=556a049578e9ec6fe972d07ab3ec59d1b2b8bcbb95c4e06b4a1c68d8067ed206:dc140c09-6a1b-11ed-8b11-795146435366; TBV=7; _pxvid=dc140c09-6a1b-11ed-8b11-795146435366; adblocked=false; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjIyNTEiLCJ0aW1lc3RhbXAiOjE2NjkwOTAzNDA4MTJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsiaWQiOm51bGwsInRpbWVzdGFtcCI6MTY2OTA5MDM0MDgxMiwiY3JlYXRlVGltZXN0YW1wIjpudWxsLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMjI1MSIsInR5cGUiOiJERUxJVkVSWSJ9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjY5MDkwMzQwODEyLCJiYXNlIjoiOTE3NDQifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YWIwNmU3NjEtNzk5Yi00NGIxLTg2MjQtZmFmNzEyYjg0NzE5In0%3D; bstc=Wfy0bnFT5zy32HEwTe_tvQ; mobileweb=0; xptc=assortmentStoreId%2B{storeID}; xpth=x-o-mverified%2Bfalse; xpa=; _astc=68e12af5a2485f61a9640813d9494eb6; pxcts=c1f0dc84-6a96-11ed-80c9-74525754424e; ak_bmsc=77058B983DAD6743D2E4D1607840369E~000000000000000000000000000000~YAAQB1LIF+KnTpuEAQAAA96uoBFVGTTDpJymd9wnhNucUQmeUSKlcG+GwPDJ2vjM+qFgjyjFynYGWU2CoZ3X2CnzUie5CrKpBUAEHiXpHaq/SpXPCPqF6r6H4iTADN3JbeH7UgVfhzIc2hkeS4CeRMcWq1gunqIk9CGnazlPgoXnrBsBVGixzJG9mGjLQv8uKxXE8pD2TbGAH6jhzCGcwXkIKwXTMTXa++nB3m97slBeFFUSBLTo15C72h4QC8Qm6xugLMacInftlMT4KltE7RQfOSXo33U9BE0m+rT29hhhlCXYhz89Ff8/iUOB2Lox1sB09aisYTjyUocTyPcBnuOv5b7pPl8eCyjEasqNyl0GfE+IPxKTcvqF1DFooZaF+xtbxjyZR0aiouoUAxDfhHtHqML1ZuBO/M4jH4SFUbabffQiLTae/zPGfBdbfml5aNnUIzT4yfPWIBkPqSPeUTmXGrT39azyF1uZcPTb4VarlJt3F/3r9glpt6Q=; wmlh=3b89c21b51eb8b365a33b532b20b3382a324d50a4d223fc09a93049c8acbe5cd; auth=MTAyOTYyMDE4Bak0%2ByYscDMh4nQihmaXma8tXP4Vh%2B65qFLv03AVr6fjsGOjMpVBt8vWmG7OTgZqZj405hB6kClT3mK8dXIR52zZ0XpW3m6Yw%2Fkb6WuvtY3ZNOG1r7BXBpEGcSn6kmks767wuZloTfhm7Wk2KcjygpySosImygUk1x1iKsdnk4%2BWTUBZJtScnjnyj6cO0BdyG7ZNY0bc90Q1Z%2F3liWmXdfgBIoW0QgNRTL3xG26qc1oUMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKrv5mz2%2FxGat%2BZvkzM5Z0PZ7AR2I8FUW05aBU8JoaK6D%2BN%2BtZ%2FlhOXSR7SRr7r1q94ym48kwO6iO63RwUR0zNXxdp65lGn5jb83oPP10O2tO1RuiPGH0mbdHq9XwQsE17KhAbajmc3a6HQbHZlS9HWyI%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTE2NzcxNzg3OCwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmFiMDZlNzYxLTc5OWItNDRiMS04NjI0LWZhZjcxMmI4NDcxOSJ9; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222254417983729%3Alastupd%3D1669147575213; xptwj=rq:ee35cdcc7e82e0c55b16:CgFls4YXhbNl7aEgKWUwyJVK/YY24e3PH3mrMN1d8e04K1bVqZOwMUwPHkZ/Ani987VkEGlvopXA/pJuDw/jS0bQhT3O5Vd6b2W4j3ocHyOh/Xc7x36fsfUbsL0zBs4WrDdJD74pvrzqFQ+wqULSWo4=; akavpau_p2=1669148175~id=d62e405f467620ad6a66e4d5f1842422; dimensionData=754; _pxff_cfp=1; com.wm.reflector="reflectorid:22222222254417983729@lastupd:1669147576000@firstcreate:1669147575213"; _px3=2fd661b00c31b0aa82683619ecabb2ef33a3823fd9a35d42209eaee8aa1f7891:qgnXmf3+wdo71HYEzSNw8cUvXJ3fegEkM5JaPQOJzr71Rn+NFFSPVCyC5QP3zQtu6QRVkkLZc3zRM1QLKu30rA==:1000:wtzGb/99ept/8eyHv9Gct32ASAadUXSH2LzM+7IaYeorsKr/Pd9eUhbNKsUfBRAVB5AQnz3w6e4xtSdNRY64/Fa0bdXwQBCnl8HL+WAymUIejXkdLSJT/fN3ob7h780/SokByA0VOYPzw5fc6NsUCUzq4lvAqYCG0iFJbjDjEBErMtvq5tTzq2ajGWp0eOG+OyWNGlovtGJTm6nXhGfMgA==; xptwg=3879158563:B9BEA7F3469380:1DDF2FA:D288B67B:61F65D39:E96DEA43:; TS012768cf=018cf40c2cd9433a6fac73c6c772129d569064457597348b893a4569872d81ec62a295443265e82271aa8099a86a84d184e06ddce2; TS01a90220=018cf40c2cd9433a6fac73c6c772129d569064457597348b893a4569872d81ec62a295443265e82271aa8099a86a84d184e06ddce2; xpm=3%2B1669147589%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; TS2a5e0c5c027=087b34fe23ab20002e92817d434d5cca0132432818e7412ba06262a4ad1aac75270423b083b54c4208585d82cb1130007ade91f79a2eeabda803aa687a8152c97dec537556b2f249fa7154d5a647f5a647d7d9d3da5fec53694d568a1bd80f52; bm_sv=987C6D61907ADD78F157C9AD177E86F0~YAAQB1LIFx+PVpuEAQAAb/zyoBFwdMwG6CBJl9MOpyC3uBhzrBOvFTU4D4BOg5guxJlXktvwTp/HC/5zM9yOklLfgTldJTnHsP7ZTJAQz46oeOi752kF+vwiYd/ArSJPoNAie9/QNeS5v0NzNTN/90vpoOrgT+1DJzE2hq+QeGUww+tmI2cswxTWRizx8Sb0N/6R+sEb1yp14LyWZqQAlZb3bKp+MLwZKY072GcOg84H2pWoR07EwF/3EHTli493ZG8=~1; ACID=547d8d74-bddd-49c4-a124-831b6c6d20f8; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS01a90220=019b75483df5ad845f3a0f54f137e5da1569c71cdfa8e270085893d59435f8050d696ff2526c9ccb73ba446186950b69c085ee0722; assortmentStoreId={storeID}; bm_sv=987C6D61907ADD78F157C9AD177E86F0~YAAQBlLIFwYh26CEAQAAJjj7oBEkZ7FexGIMn7gMDJPA5f2ybJh7Qe6rxZ8JxXRDH3FBOYsR7HDuY+t/0X7JkAmnVRr9wshYMRPn47fiWBfyqWZ1f0LLSPZ3yNsUEqdkCCCijohZva+1qW/EfedbNJgScuKAlCoyK09IUtsD5bAYywgNMkyJncIkZRShpNZ2ocG8F0peI024eet6xrikvrjLvwuQCDB9Sl2eAfiFJc3199ICIUlHdGHbVYQtWRLSA20=~1; bstc=Wfy0bnFT5zy32HEwTe_tvQ; com.wm.reflector="reflectorid:22222222254417983729@lastupd:1669148129000@firstcreate:1669147575213"; hasACID=true; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIyMjUxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0JBS0VSWSIsIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9TUEVDSUFMX0VWRU5UIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozNC4wMzA0LCJsb25naXR1ZGUiOi0xMTcuOTQwMywicG9zdGFsQ29kZSI6IjkxNzQ0IiwiY2l0eSI6IkxhIFB1ZW50ZSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjI1MSIsImRpc3BsYXlOYW1lIjoiQ2l0eSBPZiBJbmR1c3RyeSBTdXBlcmNlbnRlciIsImFjY2Vzc1BvaW50cyI6bnVsbCwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIyMjUxIiwiZGlzcGxheU5hbWUiOiJDaXR5IE9mIEluZHVzdHJ5IFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkxNzQ1IiwiYWRkcmVzc0xpbmUxIjoiMTcxNTAgR2FsZSBBdmUiLCJjaXR5IjoiQ2l0eSBPZiBJbmR1c3RyeSIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjkxNzQ1LTE4MDkifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjMzLjk5ODQzNywibG9uZ2l0dWRlIjotMTE3LjkzMjM3Nn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzdG9yZUZlZVRpZXIiOiJCIiwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyMjUxIiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY2OTExNDA0ODg3MSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjU0N2Q4ZDc0LWJkZGQtNDljNC1hMTI0LTgzMWI2YzZkMjBmOCJ9; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMjI1MSIsInRpbWVzdGFtcCI6MTY2OTA5MjQ0ODg2OH0sInNoaXBwaW5nQWRkcmVzcyI6eyJpZCI6bnVsbCwidGltZXN0YW1wIjoxNjY5MDkyNDQ4ODY4LCJjcmVhdGVUaW1lc3RhbXAiOm51bGwsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTE3NDQiLCJjaXR5IjoiTGEgUHVlbnRlIiwic3RhdGUiOiJDQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyMjUxIiwidHlwZSI6IkRFTElWRVJZIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2NjkwOTI0NDg4NjgsImJhc2UiOiI5MTc0NCJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo1NDdkOGQ3NC1iZGRkLTQ5YzQtYTEyNC04MzFiNmM2ZDIwZjgifQ%3D%3D; mobileweb=0; vtc=UGU5eVHk5EhK7aTJFJweZI; xpa=; xpm=3%2B1669148128%2BUGU5eVHk5EhK7aTJFJweZI~%2B0; xptc=assortmentStoreId%2B{storeID}; xpth=x-o-mverified%2Bfalse; xptwg=248156628:1FEBD1385B08140:52234E4:151DE32C:6C7C2091:92263C79:; xptwj=rq:56555ca0cecaad9a50da:oGFGwCY0K2WeLbtwhQuqfsPe8yki4ZhEwcJwHcNYB2sF3nCe6Sr/uor4JosU6YvG0L24SPxlS2zq8vV/b/hWsi2CoOG01oSuo5ALMdytOPNkgY2M2MpsJhM=; TS012768cf=019b75483df5ad845f3a0f54f137e5da1569c71cdfa8e270085893d59435f8050d696ff2526c9ccb73ba446186950b69c085ee0722; TS2a5e0c5c027=08013b6833ab2000212165bf28ec6de33bb70fd19c56a65466d1a589ffe859a78faa282cd4daa0d60805c3a70a1130003f8c0979ba1925403599315d49ee183de0832847477af77d72338bfa35714f867ea6d236c16323981ba15c81520356e0; _pxhd=677d0fc014d912fd62a2e7ee1192793c80bee74fc7f09625e15facdfb821f97c:c490d453-6a20-11ed-a3e9-54766f4c5843; akavpau_p2=1669148729~id=1f15f8bdd65626e4d4d687a99c9a0eb3',
            'device_profile_ref_id': 'cvqfZESMkKoPV9cVCESMqeoeHrr6UZGZoDPT',
            'referer': f'https://www.walmart.com/search?q={itemSearch}',
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
            for i in searchedItems['data']['search']['searchResult']['itemStacks']:
                searchedItems = i['itemsV2']


            itemID = {}
            itemInfo = {}

            for num,i in enumerate(searchedItems):
                try:
                    if 'name' in i.keys():
                        itemID[num] = i['name']
                        itemInfo[i['name']] = {'price' : i['priceInfo']['currentPrice'],
                                                        'imageURL': i['imageInfo'],
                                                        'description' : i['shortDescription']}
                except:
                    continue

            # print(itemID)
            #for i in itemInfo:
                #print(i,'\n',itemInfo[i],'\n\n')
            items = [itemID,itemInfo]
            return items
        except:
            return 0


    def wholefoodsItems(self,itemSearch,storeID): #add '+' between words with spaces for itemSearch
        try:
            url = f"https://www.wholefoodsmarket.com/_next/data/gA_0Z8pXk88CJBarkJ90-/search.json?text={itemSearch}&store={storeID}"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            searchedItems = json.loads(response.text)

            itemID = {}
            itemInfo = {}

            
            for num,i in enumerate(searchedItems['pageProps']['data']['results']):
                try:
                    itemID[num] = i['name']
                    itemInfo[i['name']] = {'price' : '$' + str(i['regularPrice']),
                                            'imageURL': i['imageThumbnail'],
                                            'brand': i['brand'],
                                            'description' : i['slug']}
                except:
                    continue


            #print(itemID)
            #for i in itemInfo:
                #print(i,'\n',itemInfo[i],'\n\n')
            items = [itemID,itemInfo]
            return items
        except:
            return 0

    def northgateItems(self,itemSearch,storeID): #add a '%20' as a space for itemSearch
        try:
            url = f"https://api.freshop.com/1/products?app_key=northgate_markets&fields=id%2Cidentifier%2Cattribution_token%2Creference_id%2Creference_ids%2Cupc%2Cname%2Cstore_id%2Cdepartment_id%2Csize%2Ccover_image%2Cprice%2Csale_price%2Csale_price_md%2Csale_start_date%2Csale_finish_date%2Cprice_disclaimer%2Csale_price_disclaimer%2Cis_favorite%2Crelevance%2Cpopularity%2Cshopper_walkpath%2Cfulfillment_walkpath%2Cquantity_step%2Cquantity_minimum%2Cquantity_initial%2Cquantity_label%2Cquantity_label_singular%2Cvarieties%2Cquantity_size_ratio_description%2Cstatus%2Cstatus_id%2Csale_configuration_type_id%2Cfulfillment_type_id%2Cfulfillment_type_ids%2Cother_attributes%2Cclippable_offer%2Cslot_message%2Ccall_out%2Chas_featured_offer%2Ctax_class_label%2Cpromotion_text%2Csale_offer%2Cstore_card_required%2Caverage_rating%2Creview_count%2Clike_code%2Cshelf_tag_ids%2Coffers%2Cis_place_holder_cover_image%2Cvideo_config%2Cenforce_product_inventory%2Cdisallow_adding_to_cart%2Csubstitution_type_ids%2Cunit_price%2Coffer_sale_price%2Ccanonical_url%2Coffered_together%2Csequence&include_offered_together=true&limit=24&q={itemSearch}&relevance_sort=asc&render_id=1669780382395&sort=relevance&store_id={storeID}&token=049dcfc6232677a2834be94d26ce7604"

            payload={}
            headers = {
            'authority': 'api.freshop.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.northgatepronto.com',
            'referer': 'https://www.northgatepronto.com/shop',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            searchedItems = json.loads(response.text)

            itemID = {}
            itemInfo = {}

            # for i in searchedItems['items']:
                # print(i)

            for num,i in enumerate(searchedItems['items']):
                try:
                    itemID[num] = i['name']
                    i['price'] = i['price'].replace(' for ', '')
                    itemInfo[i['name']] = {'price' : i['price'],
                                            'buyURL': i['canonical_url']
                    }

                except:
                    continue
            # print(itemID)
            # for i in itemInfo:
                # print(i,'\n',itemInfo[i],'\n\n')
            items = [itemID,itemInfo]
            return items
        except:
            return 0

    def getAllItemsWithStores(self, search):
        getitem = getItems()
        walmartItems = getitem.walmartItems(search, '3133')
        #wholefoodsItems = getitem.wholefoodsItems(search, '10594')
        northgateItems = getitem.northgateItems(search,'6097')

        allItems = []

        # adding walmart items to the array
        for k,v in walmartItems[1].items():
            entry = v
            try:
                # resolving to the common format
                price = entry['price']['priceString']
                entry['price'] = price
                
                
                
            
                imageURL = entry['imageURL']['thumbnailUrl']
                entry['imageURL'] = imageURL
                

                entry['name'] = k
                entry['store'] = 'walmart'
                allItems.append(entry) 
            except:
                continue

        # # adding walmart items to the array
        # for k,v in targetItems[1].items():
        #     entry = v

        #     try:

        #         imageURL = entry['imageURL']['primary_image_url']
        #         entry['imageURL'] = imageURL

        #         description = '<li>' + '</li><li>'.join(entry['description']) + '</li>'
        #         entry['description'] = description

        #         entry['name'] = k
        #         entry['store'] = 'target'
        #         allItems.append(entry) 
        #     except:
        #         continue


        # adding walmart items to the array
        for k,v in northgateItems[1].items():
            entry = v

            try: 
                entry['name'] = k
                print(k)

                entry['store'] = 'northgate'
                allItems.append(entry) 
            except:
                continue

        # sorting the items
        allItems.sort(key=lambda x: eval(x['price'].replace('$', '')) )
        

        return allItems

            
def getWalmartPrices(walmartItems):
        prices = []
        for x in walmartItems[1]:   #Item Info
            print ("Item: " + x)
            for y in walmartItems[1][x]:    #Keys of Item Info: shortDescription, imageURL, currentPrice
                if(y == "price"):
                    print (y,':',walmartItems[1][x][y])
                    prices.append(walmartItems[1][x][y])
                    # for key, value in walmartItems[1][x][y].items():   #Keys and values of currentPrice
                    #     print("Key= " + key, " : Val= ", value)
                    #     if(key == "price"): #Append Int price to list
                    #         prices.append(value)
                    #         #print(value)    
         
        prices.sort()   #Sort list of prices
        if(prices[0]):
            return prices[0]
        else:
            return 0


#getitem = getItems()
#walmartItems = getitem.walmartItems('broccoli', '3133')
#wholefoodsItems = getitem.wholefoodsItems('juice', '10594')
#northgateItems = getitem.northgateItems('broccoli','6097')

# cheapestWalmartPrice = getWalmartPrices(walmartItems)
# print("Cheapest price found", cheapestWalmartPrice) 

#allitems = getitem.getAllItemsWithStores('broccoli')

# print('\n\n================================')
# print(*allitems, sep="\n\n")