# STEP 1 SET UP THE PY SCRIPT
    # pip install requests
    # pip install beautifulsoup4
    # pip install pandas

    # print("Hello World")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 2 GET REQUEST TO WEBSITE - NEED RESPONSE 200
url = 'http://quotes.toscrape.com'
response = requests.get(url)
# print response

# STEP 3 COLLECT HTML AND MAKE IT TEXT
html = response.text
# print html
# the response will come back as an HTML string

# STEP 4 PARSE THE HTML WITH BEAUTIFUL SOUP
soup = BeautifulSoup(html, 'lxml')
# print soup


# STEP 5 CHECK THE WEBSITE TO LOCATE THE SELECTORS/DATA

# STEP 6 CREATE A LIST OF EVERY DIV THAT HAS A CLASS OF "QUOTE"
quote_divs = soup.find_all('div', {'class': 'quote'})
# print len(quote_divs)

# STEP 7 BREAK DOWN ONE INSTANCE FIRST
first_quote = quote_divs[0]
# print first_quote

# 7A GET TEXT
span_text = first_quote.find('span', {'class': 'text'})
quote = span_text.text
# print quote

# 7B GET AUTHOR
span_author = first_quote.find('small', {'class', 'author'})
author = span_author.text
# print author

# 7C GET AUTHOR'S BIO
author_link = span_author.findNextSibling().attrs.get('href')
author_bio_link = url + author_link
# print author_bio_link

# 7D GET THE TAGS
tag_container = first_quote.find('div', {'class': 'tags'})
tag_links = tag_container.find_all('a')

tags = []
for tag in tag_links:
    tags.append(tag.text)
# print tags

# print('text:', quote)
# print('author name:', author)
# print('author link:', author_bio_link)
# print('tags:', tags)

# STEP 8 CREATE A FUNCTION TO MAKE THE CODE REUSABLE
def quote_data(quote_div):
    #Collect the quote
    span_text = quote_div.find('span', {'class': 'text'})
    quote = span_text.text

    #Collect the author name
    span_author = quote_div.find('small', {'class', 'author'})
    author = span_author.text

    #Collect the author bio link
    author_link = span_author.findNextSibling().attrs.get('href')
    author_bio_link = url + author_link

    #Collect the tags
    tag_container = quote_div.find('div', {'class': 'tags'})
    tag_links = tag_container.find_all('a')

    tags = []
    for tag in tag_links:
        tags.append(tag.text)

    return {'author': author,
            'text' : quote,
            'author_link': author_bio_link,
            'tags': tags}

# STEP 9 TEST OUT FUNCTION
# print quote_data(quote_divs[7])

# STEP 10 SCRAPE ONE PAGE
page_one_data = []

#Iterate over each quote using for loop
for div in quote_divs:
    #Apply our function on each quote
    data_from_div = quote_data(div)
    page_one_data.append(data_from_div)

# print(len(page_one_data), "quotes scraped!")
# print page_one_data[:1]



# STEP 11 FUNCTION WITH A FUNCITON EMBEDDED
def scrape_page(quote_divs):
    data = []
    for div in quote_divs:
        div_data = quote_data(div)
        data.append(div_data)
    return data

# STEP 12 GRAB ALL QUOTES FROM ONE PAGE
data = scrape_page(quote_divs)

# STEP 13 NEXT PAGE BUTTON
pager = soup.find('ul', {'class': 'pager'})

# STEP 14 IF STATEMENT
if pager:
    next_page = pager.find('li', {'class': 'next'})


if next_page:
    next_page = next_page.findChild('a')\
                         .attrs\
                         .get('href')
# print next_page

# STEP 15 GENERATE THE FULL URL
next_page = url + next_page
# print next_page

# STEP 16 RECURSION
def scrape_quotes(url):
    base_url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    quote_divs  = soup.find_all('div', {'class':'quote'})
    data = scrape_page(quote_divs)

    pager = soup.find('ul', {'class':'pager'})
    if pager:
        next_page = pager.find('li',{'class':'next'})

        if next_page:
            next_page = next_page.findChild('a')\
                                 .attrs\
                                 .get('href')
            next_page = base_url + next_page
            print("Scraping", next_page)
            ## RECURSION
            data += scrape_quotes(next_page)
    return data


data = scrape_quotes(url)
# print(len(data), "Quotes scraped")


# STEP 17 VISUALIZE DATA WITH PANDAS - EXPORT TO CSV
df = pd.DataFrame(data)
df.to_csv('py_beautifulsoup_test.csv', encoding='utf-8')



# print("Hello")
