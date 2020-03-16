# Price-data-of-part-of-US-Stocks-in-2014-2019

价格数据通过python库yfinance取自雅虎财经，股票筛选池(eastmoney.csv，共12561支)为东方财富的美股列表(http://quote.eastmoney.com/usstocklist.html)

The price data are downloaded through a python library named 'yfinance' from Yahoo Finance.

The pool of stocks(eastmoney.csv) is crawled from the US Stocks list of Eastmoney(http://quote.eastmoney.com/usstocklist.html), the size of which is 12561.

排除以下两种无法得到数据的股票：

Excluding two types of stocks below,

(1)无法查询到数据的股票；

(1)data of which cannot be queried;

(2)在2013-12-31到2019-12-31之间无交易的股票；

(2)no activities of which happen between 2013-12-31 and 2019-12-31,

还剩9267支股票，本数据记录了这些股票在共1510个交易日内的价格。

there remain 9267 stocks, whose prices in 1510 trading days are recorded here.

* 数据的行数1510对应的交易日期见date.csv

* Number of rows of data here corresponds to 1510 trading days in date.csv

* 数据的列数9267对应的具体股票已脱敏处理，无对应股票代码

* Number of columns of data here corresponds to 9267 stocks whose symbols are desensitized.

 
----csv files----

opening_price.csv	当日开盘价

highest_price.csv	当日最高价

lowest_price.csv	当日最低价

closing_price.csv	当日收盘价


----mat file----

14_19_AmericanStocks.mat文件需在matlab中打开，包含4个1510*9267的矩阵

14_19_AmericanStocks.mat should be opened in Matlab, including four 1510*9267 matrices

Open	当日开盘价

High	当日最高价

Low 当日最低价

Close	当日收盘价

-------------------------------------

数据没有上传成功，可以发邮件到jiaoyiru@hit.edu.cn询问。

Data files fail to be uploaded, but still can be asked from jiaoyiru@hit.edu.cn. 
