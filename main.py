import requests   
import webbrowser
import bs4
n=int(input("Number of urls\n"))
score={}
for i in range (0,n):
    link=input("Enter the Qwiklab public profile URL here:\n")
    res = requests.get(link) 
    noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")   
    quests = noStarchSoup.select('div .public-profile__badge')
    name =  (noStarchSoup.select('div .public-profile__hero h1')[0].getText())[1:-1]
    print("\n name:",name)
    print("number of quests completed is:",len(quests))
    score[name]=len(quests)

print(score)

