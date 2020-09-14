# DataScience using Pandas
import pandas as pd
import numpy as np

# intialise data of lists.
symbols = ['AAPL', 'INFY', 'TCS', 'REL', 'JSL', 'JSW', 'AAPL', 'TCS', 'JSW', 'AAPL']
type = ['BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'SELL', 'BUY', 'BUY', 'BUY', 'SELL']
amt = [100, 190, 200, 110, 120, 170, 300, 210, 190, 310]
data = {'Symbol':symbols,
        'Type': type,
        'Value': amt
        }

# Create DataFrame
df = pd.DataFrame(data)
print('\n\n\n')
#df = df.groupby(["Symbol", "Type"]).agg({"Value": 'sum'}).reset_index()
df = df.groupby(["Symbol", "Type"]).agg({"Value": 'sum'}).reset_index()

df['Value'] *= np.where(df['Type']=='BUY', 1, -1)
df = df.groupby('Symbol', as_index=False).agg({'Type':'first','Value':'sum'})

# Print the output.
print(df)
print('\n\n\n')
