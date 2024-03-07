import yfinance as yf

#import requests_cache

#https://www.kaggle.com/code/ismailaliahmed/download-stocks-from-yahoofinance



#//https://github.com/ranaroussi/yfinance
#https://medium.com/@TejasEkawade/getting-indian-stock-prices-using-python-19f8c83d2015

#stocks = pd.read_html('https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_National_Stock_Exchange_of_India')[2].Symbol

#stocks = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2].Symbol
#tickers = yf.Tickers('msft,aapl,goog')
#read from file. csv with single column
tickers = ["SPY", "AAPL", "MSFT"]

#df = yf.download(stocks,start='2023-01-01')['Close']

#data = yf.download(["SPY", "AAPL", "MSFT"], period="1mo" , index_as_date = False)['Close']
data = yf.download(tickers, period="1mo")['Close']


print(data.index)
newdf = data.reset_index()

print(newdf)
#print(data.AAPL.values[1])

#Dictionary to add stock name and count of the highs

print(data)

print(data.shape)


print(newdf[['Date','AAPL']])

#loop throught tickers
for ticker in tickers:
 base_price = 0
 counter = 0
 print(ticker)
 #for each ticket get data from newdf
 #iterate over for particular ticker, set base counter = 0 and base_price of the oldest date
 #increment the counter +1 on current iteration price > base price and set the base_price to currrent iteration price.
 #inner loop finish
#outer loop:
#write record in csv
ticker


#after looping
#print(list(data.index.values))
#print(data.columns)

#for stock in data :
 #    print(data[stock].values)



#tickerStrings = ['AAPL', 'MSFT']
#df = yf.download(tickerStrings, group_by='Ticker', period='2d')
#df = df.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
#print(df)

#print(data)


