import requests
import pandas as pd

base_url = 'http://reports.okaydiagnostic.com/upload/CovidReports/'
#vai = '19472'
dash = '_'
number = '2'
suffix = '.pdf'

reports = dict()
reports['VAI'] = []
reports['URL'] = []

def getReports(startVAI, endVAI, count_init):
    count = count_init
    for vai in range(startVAI, endVAI):
        # if it's first VAI, update count!
        if vai == startVAI:
            count = findVAI_num(vai)
            fetchReport(vai, count, 0)
        else:
            count += 1
            fetchReport(vai, count, 0)

def fetchReport(vai, count, error_code):
    url = base_url + str(vai) + dash + str(count) + suffix
    res = requests.get(url)
    if res.status_code == 200:
        # append to reports dict lists
        reports['VAI'].append(f'{vai}_{count}')
        reports['URL'].append(url)

        print(f"\u001b[35m {vai}_{count}: {url} \u001b[0m")
    else:
        # Report doesn't exist at particular VAI count, try next
        if error_code == 1:
            newVAI = vai + 1
            fetchReport(newVAI, count, 1)
        # Check for count again
        elif error_code == 2:
            new_count = findVAI_num(vai)
            fetchReport(vai, new_count, 1)
        else:
            fetchReport(vai, count, 1)


"""
    Get the initial vai_num by VAI
"""
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
    try:
        getReports(19346, 19410, 0)

        # save pandas csv
        df = pd.DataFrame.from_dict(reports)
        df.to_csv('okay.csv')

    except KeyboardInterrupt as ki:
        # save pandas csv
        df = pd.DataFrame.from_dict(reports)
        df.to_csv('okay.csv')
