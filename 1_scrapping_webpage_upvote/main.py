import requests       # -> module that helps in requesting url
from bs4 import BeautifulSoup

# step 1 -geetting url
url = "https://news.ycombinator.com/news"            # ->link saved in var name url
response = requests.get(url)
web_page = response.text

# step 2 -geeting content
soup = BeautifulSoup(web_page, "html.parser")

all_anchor_tags = soup.find_all('a', class_="storylink")  # searching all anchor tag that start with class =storylink

# saving all anchor text and link in list
article_texts = []
article_links = []
for anchor_tag in all_anchor_tags:
    text = anchor_tag.getText()        # extracting text from anchor tag
    article_texts.append(text)         # adding that in the list

    link = anchor_tag.get("href")      # extracting link from anchor tag
    article_links.append(link)

#same process aa above
all_upvotes = soup.find_all("span", class_="score")
upvotes =[]
for upvote in all_upvotes:
    up = upvote.getText()        # [78 vote]
    num_up = int(up.split()[0])  #-> ['78', 'vote']   -> 78
    upvotes.append(num_up)

largest_number = max(upvotes)
index_largest = upvotes.index(largest_number)


print (article_texts[index_largest])
print (article_links[index_largest])
print(upvotes[index_largest])
