import webbrowser
import bs4
import asyncio
import aiohttp
from dictator import create_dict

score={}
quest_list=["Perform Foundational Infrastructure Tasks in Google Cloud","Set up and Configure a Cloud Environment in Google Cloud","Deploy and Manage Cloud Environments with Google Cloud","Build and Secure Networks in Google Cloud","Deploy to Kubernetes in Google Cloud","Getting Started: Create and Manage Cloud Resources","Perform Foundational Data, ML, and AI Tasks in Google Cloud","Insights from Data with BigQuery","Engineer Data in Google Cloud","Integrate with Machine Learning APIs","Explore Machine Learning Models with Explainable AI"]

async def scrape(name, url):
    quest_completed=[]
    quest_count=0

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            res = await resp.text()

    # res = requests.get(link) 
    noStarchSoup = bs4.BeautifulSoup(res,"html.parser")   
    badges_divs = noStarchSoup.find_all("ql-badge")
    
    quest_count=0
    for badge in badges_divs:
        b = badge.get("badge")
        title = b[22:b.index('\",\"', 22)]
        #print(title)
        if title in quest_list:
            quest_count+=1

    return dict({ 'name': name, 'count': quest_count })


def get_board():
    score = create_dict()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks=[]

    for name,qwik in score.items() :
        tasks.append(scrape(name, qwik))

    if tasks != []:
        try:
            done, pending = loop.run_until_complete( asyncio.wait(tasks))

            for future in done:
                value = future.result()
                name = value['name']
                quest_count = value['count']
                score[name]=quest_count
        
        except Exception as e:
            print(str(e))

    print(str(score))

    sort_orders = sorted(score.items(), key=lambda x: x[1], reverse=True)
    i=0
    for i in range(0,len(sort_orders)):
        if(int(sort_orders[i][1])>0):
            i=i+1
        else:
            break
    return sort_orders[0:i]


get_board()