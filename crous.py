#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
from datetime import date

print("\n###########################################")
print("\nMenu du jour au RU : Le Lac")
print("\nCreated by Simon Rogé, last update : January 18th, 2022\n\n")

html_doc = requests.get('http://www.crous-orleans-tours.fr/restaurant/le-lac').content
soup = BeautifulSoup(html_doc,features="lxml")

def translate(month):
    if month == "January":
        return "janvier"
    elif month == "February":
        return "février"
    elif month == "March":
        return "mars"
    elif month == "April":
        return "avril"
    elif month == "May":
        return "mai"
    elif month == "June":
        return "juin"
    elif month == "July":
        return "juillet"
    elif month == "August":
        return "août"
    elif month == "September":
        return "septembre"
    elif month =="October":
        return "octobre"
    elif month =="November":
        return "novembre"
    elif month =="December":
        return "décembre"

def translateDay(day):
    if day =="Monday":
        return "lundi"
    elif day =="Tuesday":
        return "mardi"
    elif day == "Wednesday":
        return "mercredi"
    elif day == "Thursday":
        return "jeudi"
    elif day == "Friday":
        return "vendredi"
    elif day == "Saturday":
        return "samedi"
    elif day == "Sunday":
        return "dimanche"


today = date.today().strftime("%A %d %B %Y")
strdate = str(today)
split = strdate.split(' ')
split[0]= translateDay(split[0])
split[2] = translate(split[2])

strdate =""
for i in range(4):
    strdate += split[i]
    if i<3:
        strdate +=' '

print("Menu du " + strdate +'\n')

index= "<h3>Menu du "+strdate+"</h3>"

for p in soup.find_all('h3'):
    if str(p)==index:
        menu = p

menuDuJour = menu.parent.contents[3].find(string="Déjeuner").parent.parent
k=0
for i in menuDuJour.find_all('span'):
    
    print('------------')
    print(i.string)
    print('------------\n')

    for z in menuDuJour.find_all('ul')[k].find_all('li'):
        print(z.string)
    print()
    k+=1