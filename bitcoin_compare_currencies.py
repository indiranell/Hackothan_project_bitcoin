import matplotlib.pyplot as plt
import pandas as pd
import quandl

#Quandl api key
quandl.ApiConfig.api_key = 'HbS8azUsnsRnb_d17E1Z'

#Read different markets for USD
df_usd_bitstamp = quandl.get("BCHARTS/BITSTAMPUSD", start_date="2016-09-12", end_date="2017-10-12", returns="pandas")
df_usd_kraken = quandl.get('BCHARTS/KRAKENUSD',start_date="2016-09-12", end_date="2017-10-12", returns="pandas")
print ("Program starts here")
#Plot using matplotlib library
f, (ax1, ax2) = plt.subplots(1, 2)
plt.suptitle("Bitcoin Open and close Price of different markets in USD")
ax1.set_title('BITSTAMP Market')
ax2.set_title('KRAKEN Market')
#Plot BITSTAMP
plt.legend(['Open','Close'], loc='upper right')
ax1.plot(df_usd_bitstamp[['Open']], color='r')
ax1.plot(df_usd_bitstamp[['Close']], color='g')
ax1.set_xlabel('Year', size =14,va = 'center')
ax1.set_ylabel('Price(in USD)', size =14,va = 'center')
#Plot KRAKEN
ax2.plot(df_usd_kraken[['Open']], color='r')
ax2.plot(df_usd_kraken[['Close']], color='g')
ax2.set_xlabel('Year', size =14,va = 'center')
ax2.set_ylabel('Price(in USD)', size =14,va = 'center')
plt.legend()

#data[['High','Low','Open','Close']].plot()
#plt.show()
plt.show()
