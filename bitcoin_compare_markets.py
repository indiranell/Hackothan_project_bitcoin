import matplotlib.pyplot as plt
import pandas as pd
import quandl
# Using Matplotlib to plot different markets in US

#Quandl api key
quandl.ApiConfig.api_key = 'HbS8azUsnsRnb_d17E1Z'

# Pull pricing data for 3 more BTC exchanges
exchanges = ['COINBASE','BITSTAMP','ITBIT','KRAKEN']

exchange_data = {}
print ("Exchange code starts here")
for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    btc_exchange_df = quandl.get(exchange_code)
    exchange_data[exchange] = btc_exchange_df

def merge_dfs_on_column(dataframes, labels, col):
    #Merge a single column of each dataframe into a new combined dataframe
    series_dict = {}
    for index in range(len(dataframes)):
        series_dict[labels[index]] = dataframes[index][col]
        
    return pd.DataFrame(series_dict)

df_usd_datasets = merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')

print (df_usd_datasets.tail())

df_usd_datasets.plot()
plt.title("Bitcoin Price (USD) comparision for different markets")
plt.show()
