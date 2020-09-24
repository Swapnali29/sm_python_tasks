import requests
from bs4 import BeautifulSoup

page = requests.get("https://news.ycombinator.com/")

print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

news_titles_list = soup.find_all(class_='storylink')

# for news_titles in news_titles_list:
#     print(news_titles)

for names in news_titles_list:
    titles = names.contents[0]

    print(titles)

ns_path = input("enter the file name or file path where you want to save the news:")

f = open(ns_path,'w') #here  can be append mode or write mode bcz write overwrites in the file & append mode appends to exiting data

f.write(titles)

f.close()