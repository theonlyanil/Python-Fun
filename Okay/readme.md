# Okay Diagnostics Reports Helper
This script lets you download your covid19 report from Okay Diagnostics Lab with VAI number as input instead of VAI+Full_Name on their website.

## How to get your report
- Run 'python3 reports.py' in Terminal
- Enter start & end VAI range as your VAI number and VAI number+1, respectively.
- You will see a result in Terminal printed with a magenta text, if that report exists.

## How to get multiple reports
- Run 'python3 reports.py' in Terminal
- Enter start & end VAI range e.g. 19000, 19100 (This fetches 100 reports)
- You will see results in Terminal in a magenta text with a URL.
- If the program is stopped, it will save all fetched reports in a CSV file (okay.csv) with VAI and report URL.
