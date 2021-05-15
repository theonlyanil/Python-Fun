import streamlit as st
import pandas as pd
import requests
st.title('Cowin Data')

district_id = st.text_input('District ID', 505)
date = st.date_input('Date').strftime('%d-%m-%Y')

url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}'

agent = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,hi;q=0.9",
    "if-none-match": '"W/"55fd-AWNhCgGMLTsXcejSn31biThNdD8""',
    "origin": "https://www.cowin.gov.in",
    "referer": "https://www.cowin.gov.in/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

session = requests.Session()
reque = session.get('https://www.cowin.gov.in/home', headers=agent)
cookies = dict(reque.cookies)

req = session.get(url, headers=agent, cookies=cookies)
session.cookies.clear()
centers = req.json()['centers']
books = []
for center in centers:
    booked = center['sessions'][0]['available_capacity']
    if booked == 0:
        booked = 'Booked'
    else:
        booked = 'Available'
    books.append(booked)

print(books)
df = pd.DataFrame(centers)
df['Availability'] = pd.Series(books)
df = df[['Availability', 'center_id', 'name', 'address', 'state_name', 'district_name', 'block_name', 'pincode', 'from', 'to', 'fee_type']]
df

#for x in range(37):
#    url = f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{x}'
#    req = session.get(url, headers=agent, cookies=cookies)
#    res = req.text
#    res
