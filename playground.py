# Version 3.6.1
# https://documentation.tradier.com/brokerage-api/markets/get-quotes

import requests
import pprint as pp

#Returns the option chain
# optionChain = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
#     params={'symbol': 'WMT', 'expiration': '2019-08-30'},
#     headers={'Authorization': 'Bearer rEXSXjMZ1h3t2xowebYQhExSEWXK', 'Accept': 'application/json'})
#
# optionChain_response = optionChain.json()
# pp.pprint(optionChain.status_code)
# pp.pprint(optionChain_response)

#Returns Options Strikes
# response = requests.get('https://sandbox.tradier.com/v1/markets/options/strikes',
#     params={'symbol': 'VXX', 'expiration': '2019-05-17'},
#     headers={'Authorization': 'Bearer rEXSXjMZ1h3t2xowebYQhExSEWXK', 'Accept': 'application/json'}
# )
# json_response = response.json()
# print(response.status_code)
# print(json_response)

# Returns the Stock Quote and Other Info

def fetchStockInfo(stock):
    stockQuote = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
        params={'symbols': stock},
        headers={'Authorization': 'Bearer DBbN23G7GxgYXqli6PcLe7DqK7kF', 'Accept': 'application/json'}
    )
    stock_response = stockQuote.json()
    ask = stock_response['quotes']['quote']

    return ask

def getExpDates(stock):
    #Returns the option expirations
    response = requests.get('https://sandbox.tradier.com/v1/markets/options/expirations',
        params={'symbol': stock, 'includeAllRoots': 'true', 'strikes': 'true'},
        headers={'Authorization': 'Bearer DBbN23G7GxgYXqli6PcLe7DqK7kF', 'Accept': 'application/json'}
    )
    json_response = response.json()
    print(response.status_code)

    dateDict = []

    #Pulls the dates for the selected stock
    for k in json_response['expirations']['expiration']:
        dateDict.append(k['date'])

    return dateDict

#Returns the option chain
def getOptionChain(stock):
    optionChain = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
        params={'symbol': stock, 'expiration': '2019-10-25'},
        headers={'Authorization': 'Bearer DBbN23G7GxgYXqli6PcLe7DqK7kF', 'Accept': 'application/json'})

    optionChain_response = optionChain.json()
    pp.pprint(optionChain.status_code)

    chain = []

    for k in optionChain_response['options']['option']:
        chain.append(k)

    return chain
