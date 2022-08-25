from bs4 import BeautifulSoup                            # imported to pull info from coinmarketcap
import requests                                          # request module to pull requests 

url = "https://coinmarketcap.com/"                       
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody                                        # passes tbody in HTML to a variable 
trs = tbody.contents



prices = {}

for tr in trs[:10]:                                      # a for loop to pull the info 
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    
    
    prices[fixed_name] = fixed_price
    

for name in prices:                                     # this for statement prints the cryptocurrencies vertically.
    print(name,": ",prices[name])
    
    
    
    
"--------------------"
"eventually add on"
#visualize the data with seaborn 
#Put the info in a table 