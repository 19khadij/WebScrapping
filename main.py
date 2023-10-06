# Scrape a website:
# 1. Use API
# 2. HTML web scrapping using some tool like bs4

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#Get the HTML
r = requests.get(url) #need url content
htmlContent =  r.content
# print(htmlContent)

#Parse the HTML
##Creating soup
soup= BeautifulSoup(htmlContent,'html.parser')
prettified_html = soup.prettify()  # Add () here to call the prettify method
# print(prettified_html)

#HTML tree traversal
##Commonly used types of object
# print(type(title)) #1.Tag
# print(type(title.string))
# #2.NAvigableString
# print(type(soup)) #3.BEautifulSoup
#4.Comment

# Get the title of HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)


#get classes of any element in HTML page
# print(soup.find('p')['class'])

#find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

#Get all anchor tags
anchors = soup.find_all('a')
#Get all the links on the page
all_links=set()
for link in anchors:
    if link.get('href')!= '#':
        linkT = 'https://codewithharry.com'+link.get('href')
        all_links.add(link)
        # print(linkT)
# print(anchors)

# markup = "<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(type(soup2.p.string))
# exit()


# . content- A tag's children are avialable as alist
# . chilldren - A tag's children are available as a generator
div=soup.find(id="imgpreview2")
for elm in div.children:
    print(elm)
# print(div.child)


