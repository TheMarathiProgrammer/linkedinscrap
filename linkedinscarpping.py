from bs4 import BeautifulSoup
import requests,sqlite3,re

url = "https://in.linkedin.com/jobs/jobs-in-pune?trk=homepage-basic_intent-module-jobs&f_TPR=r86400&position=1&pageNum=0&currentJobId="
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)
page = soup.find(class_="results__list")
# print(page)
page1 = page.find_all(class_='result-card__full-card-link')
jobtitle1 = []
for j in page1:
	page2 = j.find_all('span')
	for i in page2:
		jobtitle1.append(i.get_text())
page3 = page.find_all(class_='result-card__subtitle-link job-result-card__subtitle-link')
# print(job_title)
# print(len(job_title))
company_name = [i.get_text() for i in page3]
# print(company_name)
# print(len(company_name))
page4 = page.find_all(class_='job-result-card__location')
company_location = [i.get_text() for i in page4]
# print(company_location)
# print(len(company_location))
result = [item['data-id'] for item in soup.find_all('li', attrs={'data-id' : True})]
# for jid in result:
# 	url1 = url+jid
# 	p = requests.get(url1)
# 	soup1 = BeautifulSoup(p.content,'html.parser')
# 	p = soup.find(class_='results__detail-view')
# 	print(p)

conn = sqlite3.connect('job1.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jobs(Jobtitle TEXT, Company TEXT, Location TEXT)')
for i in range(len(jobtitle1)):
	cursor.execute('INSERT INTO jobs(Jobtitle,Company,Location) VALUES(?,?,?)',(jobtitle1[i],company_name[i],company_location[i]))
conn.commit()
conn.close()
