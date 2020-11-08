import requests
from bs4 import BeautifulSoup

def ctc():
	url = "https://www.google.com/search?q=dolar+hoje&oq=dolar+hoje&aqs=chrome.0.69i59j35i39j0j69i60l2.5136j0j9"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	all_table = soup.find_all(class_= 'BNeawe iBp4i AP7Wnd')
	list = "final"
	e1= str(all_table) + str(list)
	e2 = (e1) + (list)
	e3 = (e2[72:76:]).upper()
	e4 = e3. replace( ',' , '.')
	dolar =  float(e4)
	print(f"U$:{dolar}")
	
ctc()
