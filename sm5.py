# Task 5 # Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.


import requests
from bs4 import BeautifulSoup

page = requests.get("https://news.ycombinator.com/")

print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

news_titles_list = soup.find_all(class_='storylink')
# print(news_titles_list)

# for news_titles in news_titles_list:
#     print(news_titles)

for names in news_titles_list:
    titles = names.contents[0]

    print(titles)