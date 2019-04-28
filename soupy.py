    #requests- allows us to access various resources from the web
#bs4-parse internet information
import requests
from bs4 import BeautifulSoup

 #we use the get function from reqeusts
 #to access a webpage as an argument
'''
result=requests.get("https://www.google.com")
''' 
#to make sure the website is accessible
#we'll check the status code
# if its 200, it's OK
'''
print(result.status_code)
'''
#look up wikipedia page for list of http status codes for more info
#next, we print the http header of the website to see if 
#we have indeed accessed the correct website
'''
print(result.headers)
'''
#check out http headers on wikipedia
#next, we'll extract some content from the website that we accessed
'''
src=result.content
print(src)
'''
#now we'll use beautiful soup to parse the content that we gained
# we create a beautiful soup object from the src variable
'''
soup=BeautifulSoup(src,'lxml')
'''
# now we can specify instructions to access
#information directly
#the 'a' tags in an lxml file are the links so let's
#print them out shall we
'''
links=soup.find_all("a")
print("LINKS:")
print(links)
print("\n")
'''
#Perhaps we just want to 
#extract the link that contains the text "About"
# on the page instead of every single link
#We use the text function to access
#the text content between <a> and </a> tags
'''
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs["href"])
'''
#look up html attributes
#our next link is
#https://www.whitehouse.gov/briefings-statements/
#our goal: Ectract all the links off the page that point to
#briefings and statements
'''
result=requests.get("https://www.whitehouse.gov/briefings-statements/")
print(result.status_code)
src=result.content
soup=BeautifulSoup(src,"lxml")

url=[]
for h2_tag in soup.find_all("h2"):
    a_tag=h2_tag.find("a")
    url.append(a_tag.attrs["href"])
print(url)
'''
#Now we'll go through BeautifulSoup Objects

html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""
with open('index.html','w') as f:
    f.write(html_doc)

soup=BeautifulSoup(html_doc,'lxml')
#BeautifulSoup.Prettify prints out our input as 
#nicely formatted html
print(soup.prettify())
#Now, we'll cover TAGs
#so if i want to print the content that is in bold <b></b> tag
print(soup.b)
#find finds the first occurence of our tag
print(soup.find('b'))
#find_all finds all occurences of our tag
print(soup.find_all('b'))
#Now we'll cover the Name of a tag
print(soup.b.name)
#output:b
#We can also alter the name of a tag 
#and have it reflected in the source
tag=soup.b
print(tag)
tag.name="blockquote"
print(tag)
#next we'll use ATTRIBUTES
tag=soup.find_all("b")[2]
print("lol:",tag)
#we have an attribute called 'id'
# so we can print that using
print(tag.attrs['id'])
#or we can also use
print(tag["id"]) 
#it's the same thing
print(tag.attrs) #prints out all the attributes
print(tag['another-attribute'])
#we can also use del to remove attributes
#del tag['id']

#NavigableTag
tag=soup.find_all('b')[2]
print("new:",tag)
print("new string",tag.string)#this lets us get the string text in the
#html line
tag.string.replace_with("This is another string")
print(tag.text)
