# Version 3.6.1
# https://documentation.tradier.com/brokerage-api/markets/get-quotes

import requests
import pprint as pp
import json


#Returns the option chain
def getOptionChain(stock):
    optionChain = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
        params={'symbol': 'WMT', 'expiration': '2019-09-20'},
        headers={'Authorization': 'Bearer DBbN23G7GxgYXqli6PcLe7DqK7kF', 'Accept': 'application/json'})

    optionChain_response = optionChain.json()
    pp.pprint(optionChain.status_code)

    chain = []

    for k in optionChain_response['options']['option']:
        chain.append(k)

    pp.pprint(chain)

getOptionChain('aapl')
