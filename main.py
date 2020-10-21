import requests
from bs4 import BeautifulSoup

#https://www.johnlewis.com/herman-miller-aeron-office-chair-graphite/p3177252
#<p class="price price--large">£1,099.00 </p>

#Making a get request to a website
request = requests.get("https://www.johnlewis.com/herman-miller-aeron-office-chair-graphite/p3177252")
#store the contents of the request in a variable
content = request.content

#use beautifulsoup to find the elements 
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p",{"class":"price price--large"} )

#get the price and strip all formats
string_price = element.text.strip("£").replace(",","")

#integer of price
print(string_price)




