import csv
symbol=csv.reader(open("eastmoney.csv",'r'))
symbol=list(symbol)
symbols=[]
for i in range(len(symbol)):
	symbols.append(symbol[i][0])
print("length= %d"%(len(symbols)))	
import yfinance as yf
import pandas as pd
data=yf.download(symbols,start="2014-01-01",end="2019-12-31",group_by="ticker")
data.to_csv("data.csv",encoding='utf-8')

# you could split the stock list(symbols) 
# to several separate lists with shorter length, 
# so that it will be easier to download and save data.