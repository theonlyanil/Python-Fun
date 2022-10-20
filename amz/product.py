import requests
from bs4 import BeautifulSoup


link = input("Amazon URL: ") or "https://www.amazon.in/AMUL-ALMONDO-Pack-of-3/dp/B0816FY474/ref=rvi_sccl_3/260-2125556-0009724?pd_rd_w=zPJdB&content-id=amzn1.sym.59eebe5b-59e3-4882-b364-90a7b22774a2&pf_rd_p=59eebe5b-59e3-4882-b364-90a7b22774a2&pf_rd_r=MYY462YH4HMQSQ9YGF6W&pd_rd_wg=WZcX1&pd_rd_r=3e3899b9-a09e-4342-8b2a-6eaf5260357a&pd_rd_i=B0816FY474&psc=1"

site = link.split('/')[2]
code = link.split('dp')[1].split("/")[1]
url = "https://" + site + "/dp/" + code
print(url)

"""Amazon Fix"""
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


session = requests.Session()
reque = session.get("https://amazon.in", headers=HEADERS)
cookies = dict(reque.cookies)

response = session.get(url, headers=HEADERS, cookies=cookies)
session.cookies.clear()
""""""

#print(response.request.headers)
#print(response.text)


soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id="productTitle").string.strip()
print("TITLE: " + title)
price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
print("PRICE: " + price)
cat = soup.find("a", attrs={'class' : "a-link-normal a-color-tertiary"}).string.strip()
print("Cat: " + cat)
#img_url = soup.find(id="imageBlock").string
img_url = soup.find("img", attrs={"class":"a-dynamic-image a-stretch-horizontal"}).string.strip()
print("IMG: " + img_url)
