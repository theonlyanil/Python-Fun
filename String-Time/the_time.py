"""
    A fun python project which prints time in Terminal in String format.
    e.g.: 01:02:23 would be 'One past Two minutes Twenty-Three seconds'

    Bugs:
    - Doesn't differentiate b/w singular and plural words like one second
      is written as one seconds.
"""

import time
starttime = time.time()

timeDict = {'00': 'Zero', '01': 'One', '02': 'Two', '03': 'Three', '04': 'Four',
            '05': 'Five', '06': 'Six', '07': 'Seven', '08': 'Eight',
            '09': 'Nine', '10': 'Ten', '11': 'Eleven', '12': 'Twelve',
            '13': 'Thirteen', '14': 'Forteen', '15': 'Fifteen', '16': 'Sixteen',
            '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen', '20': 'Twenty',
            '21': 'Twenty-One', '22': 'Twenty-Two', '23': 'Twenty-Three',
            '24': 'Twenty-Four', '25': 'Twenty-Five', '26': 'Twenty-Six',
            '27': 'Twenty-Seven', '28': 'Twenty-Eight', '29': 'Twenty-Nine',
            '30': 'Thirty', '31': 'Thirty-One', '32': 'Thirty-Two',
            '33': 'Thirty-Three', '34': 'Thirty-Four', '35': 'Thirty-Five',
            '36': 'Thirty-Six', '37': 'Thirty-Seven', '38': 'Thirty-Eight',
            '39': 'Thirty-Nine', '40': 'Forty', '41': 'Forty-One',
            '42': 'Forty-Two', '43': 'Forty-Three', '44': 'Forty-Four',
            '45': 'Forty-Five', '46': 'Forty-Six', '47': 'Forty-Seven',
            '48': 'Forty-Eight', '49': 'Forty-Nine', '50': 'Fifty',
            '51': 'Fifty-One', '52': 'Fifty-Two', '53': 'Fifty-Three',
            '54': 'Fifty-Four', '55': 'Fifty-Five', '56': 'Fifty-Six',
            '57': 'Fifty-Seven', '58': 'Fifty-Eight', '59': 'Fifty-Nine',
            '60': 'Sixty'}


def stringTime(timeHHMMSS):
    # break it into Hour, Minute and Second
    timeList = timeHHMMSS.split(":")
    hour = timeList[0]
    min = timeList[1]
    sec = timeList[2]

    hourString = timeDict[hour]
    minString = timeDict[min]
    secString = timeDict[sec]

    if(timeDict[min] == 'Zero'):
        return f"{hourString} O'clock"
    elif(timeDict[sec] == 'Zero'):
        return f"{hourString} hours {minString} minutes"
    else:
        return f"{hourString} hours {minString} minutes {secString} seconds"

while True:
    current_time = time.strftime('%I:%M:%S', time.localtime())
    stringy = stringTime(current_time)
    print(stringy.title())

    #Do this after every second...
    time.sleep(1.00 - ((time.time() - starttime) % 1.0))
