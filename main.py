import requests   
import webbrowser
import bs4
from dictator import create_dict

score={}
quest_list=["Perform Foundational Infrastructure Tasks in Google Cloud","Setup and Configure a Cloud Environment in Google Cloud","Deploy and Manage Cloud Environments with Google Cloud","Build and Secure Networks in Google Cloud","Deploy to Kubernetes in Google Cloud","Getting Started: Create and Manage Cloud Resources","Perform Foundational Data, ML, and AI Tasks in Google Cloud","Insights from Data with BigQuery","Engineer Data in Google Cloud","Integrate with Machine Learning APIs","Explore Machine Learning Models with Explainable AI"]
def get_board():
    score = create_dict()

    for name,qwik in score.items() :
        quest_completed=[]
        quest_count=0
        link=qwik
        res = requests.get(link) 
        noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")   
        quests = noStarchSoup.select('div .public-profile__badge')
        #name =  (noStarchSoup.select('div .public-profile__hero h1')[0].getText())[1:-1]
        badges=noStarchSoup.select('div .public-profile__badge div')
        for i in range (1,len(badges)-1,3):
            quest_completed.append(badges[i].getText()[1:-1])
        for k in quest_completed:
            if (k in quest_list):
                quest_count=quest_count+1

        score[name]=quest_count

    sort_orders = sorted(score.items(), key=lambda x: x[1], reverse=True)
    return sort_orders[0:20]


get_board()

