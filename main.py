import requests   
import webbrowser
import bs4
link=input("Enter the Qwiklab public profile URL here:\n")
res = requests.get(link) 
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")   
elems = noStarchSoup.select('div .public-profile__badge')
print("number of quests completed is:",len(elems))