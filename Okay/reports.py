import requests
from pprint import pprint

base_url = 'http://reports.okaydiagnostic.com/upload/CovidReports/'
#vai = '19472'
dash = '_'
number = '2'
suffix = '.pdf'


def findByVAI(vai):
    for i in range(0, 100):
        url = base_url + str(vai) + dash + str(i) + suffix
        res = requests.get(url)
        if res.status_code == 200:
            print(f"\u001b[32m {i} Found Report \u001b[0m")
            break
        else:
            print(f"\u001b[31m {i} Not found \u001b[0m")

#findByVAI(19451)
findByVAI(input("VAI: "))
