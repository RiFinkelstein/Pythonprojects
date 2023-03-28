import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.nytimes.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and store them in a list
article_titles = []
for article in soup.find_all('article'):
    title = article.find('h2', {'class': 'css-1j9dxys e1xfvim31'})
    if title is not None:
        article_titles.append(title.text)

# Write the article titles to a text file
with open('nytimes_article_titles.txt', 'w') as f:
    for title in article_titles:
        f.write(title + '\n')
