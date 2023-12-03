from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/js/"
result = requests.get(url)

content = result.text
soup = BeautifulSoup(content, 'html.pa rser')
tag_list = soup.findAll('a', class_='tag')
print(tag_list)
# for tag in tag_list:
#     print()



# from bs4 import BeautifulSoup
# import requests


# url = "https://elitehubs.com/search?q=razer%20mouse"
# result = requests.get(url) 
# print(result) #status code == 200
# #print(result)
# html_content = result.text
# doc = BeautifulSoup(html_content, 'lxml')

# micecontainer = doc.find('div', class_ = 'collection resultListing')
# mice = micecontainer.find_all('div', class_ = 'card-information__wrapper text-left')
# print(mice)



# #print(req)
# main = soup.find('main')
# jobscontainer = main.find(id='listContainer')
# print(jobscontainer)
#jobs = jobscontainer.findAll("div", class_ = "cust-job-tuple layout-wrapper lay-2 sjw__tuple")
#print(jobs.text)

