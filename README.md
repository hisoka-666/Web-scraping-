# Web-scraping-
One way to do a data scraping without using an api just using google

## installation
first in python, you must install some libraries, to install them:
>pip install requests

>pip install bs4

>pip install lxml

### How to extract data
```
import requests
from bs4 import BeautifulSoup

Url = "your-url"
Data = requests.get(url)
Soup = BeautifulSoup(data.text,"lxml")
```
### how to filter the data
These data are still very confused you need to filter them
```
#To filter you can use
#Inside ('') you can pass tags and classes
Filter1 = soup.find_all('')
Filter2 = soup.find('')
#loop
for i in data:
    Soup.find('')
```
We can use the `decompose ()` method to exclude unwanted classes

### useful links
[BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[Requests documentation](https://requests.readthedocs.io/en/master/)
