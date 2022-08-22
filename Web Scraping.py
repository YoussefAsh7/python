# 1st step install and import modules

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

top_jop= []
company = []
location = []
skills = []
days = []
# 2nd step use requests to fetch the URL

result = requests.get(r"https://wuzzuf.net/search/jobs/?q=data+analysis&a=hpb")


# 3rd step save page content

src = result.content

# 4th step create soup object to parse contnet

soup = BeautifulSoup(src , "lxml")

# 5th step find the elements containing info we need [jop_titel , company_name , jop_location , jop_skills]

jops = soup.find_all("h2" , {"class" : "css-m604qf" } )
company_name = soup.find_all("a" , {"class" : "css-17s97q8" , "rel" : "noreferrer" } )
jop_location = soup.find_all("span" , {"class" : "css-5wys0k" } )
days_date = soup.find_all("div" ,class_= "css-4c4ojb")
jop_skills = soup.find_all("div" , {"class" : "css-y4udm8" } )


# 6th step loop over reterned lists to extract info needed 


for i in range(len(days_date)):
    top_jop.append(jops[i].text)
    company.append((company_name[i].text)[:-2])
    location.append(jop_location[i].text)
    days.append(days_date[i].text)
    skills.append(jop_skills[i].text)



# 7th step creat csv file and file it with values

file_list = [top_jop , company , location , days , skills ]
exported = zip_longest(*file_list)

with open(r"C:\Users\PCM\Desktop\first python\Jops.csv" , "w") as my_file:
    wr = csv.writer(my_file)
    wr.writerow(["Jop Titel" , "Company Name" , "Jop Location" , "Date" ,"Jop Skills"] )
    wr.writerows(exported)
