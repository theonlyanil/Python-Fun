"""
    Status: Not working...
"""
import requests
from bs4 import BeautifulSoup

baseurl = 'https://emailcrawlr.com/lookup'

response = requests.post(baseurl, data={'authenticity_token':'930K59j1Mw/EHfza5VSOkrko5nyPLInwR9r0brDiGP9aNH/RNHhV5FmS4kd60YUtOBrwOh6B1/x2omaFehEu5g==',
                                        'domain': 'widefide.com'})
print(response.text)
