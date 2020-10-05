import requests   
import webbrowser
import bs4
n=int(input("Number of urls\n"))
score={}
quest_list=["Perform Foundational Infrastructure Tasks in Google Cloud","Setup and Configure a Cloud Environment in Google Cloud","Deploy and Manage Cloud Environments with Google Cloud","Build and Secure Networks in Google Cloud","Deploy to Kubernetes in Google Cloud","Getting Started: Create and Manage Cloud Resources","Perform Foundational Data, ML, and AI Tasks in Google Cloud","Insights from Data with BigQuery","Engineer Data in Google Cloud","Integrate with Machine Learning APIs","Explore Machine Learning Models with Explainable AI"]
for i in range (0,n):
    quest_completed=[]
    quest_count=0
    link=input("Enter the Qwiklab public profile URL here:\n")
    res = requests.get(link) 
    noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")   
    quests = noStarchSoup.select('div .public-profile__badge')
    name =  (noStarchSoup.select('div .public-profile__hero h1')[0].getText())[1:-1]
    print("\n name:",name)
    badges=noStarchSoup.select('div .public-profile__badge div')
    j=0
    for i in badges:
        if (j%3==1):
            quest_completed.append(i.getText()[1:-1])
        j=j+1
    for i in quest_completed:
        if (i in quest_list):
            quest_count=quest_count+1
    print("number of quests completed is:",len(quests))
    score[name]=quest_count

sort_orders = sorted(score.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])

