# DataScience using Pandas
import pandas as pd
import numpy as np

# intialise data of lists.
symbols = ['AAPL', 'INFY', 'TCS', 'REL', 'JSL', 'JSW', 'AAPL', 'TCS', 'JSW', 'AAPL']
type = ['BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'SELL', 'BUY', 'BUY', 'BUY', 'SELL']
amt = [100, 190, 200, 110, 120, 170, 300, 210, 190, 310]
qty = [10, 8, 6, 3, 2, 8, 26, 9, 9, 28]
data = {'Symbol':symbols,
        'Type': type,
        'Value': amt,
        'Qty': qty
        }

# Create DataFrame
df = pd.DataFrame(data)

#The below code tells that if type column is buy, multiply value column by 1 else by -1
df['Value'] *= np.where(df['Type']=='BUY', 1, -1)
df['Qty'] *= np.where(df['Type']=='BUY', 1, -1)
df = df.groupby('Symbol').agg({'Value':'sum', "Qty": 'sum'})

# Print the output.
print(df)
