#!/usr/bin/env python

"""
Client for Yahoo Finance to retrieve ticker
"""

import logging
import requests
import json
import sys


logger = logging.getLogger()
logger.setLevel(logging.WARN)


class YahooFinance():
    base_url = \
        'http://d.yimg.com/autoc.finance.yahoo.com/autoc' \
        '?query={0}&callback=YAHOO.Finance.SymbolSuggest.ssCallback'
    stockr_exchanges = ['NYSE', 'NASDAQ']
    yahoo_response_string = 'YAHOO.Finance.SymbolSuggest.ssCallback('

    def get_ticker(self, company_name):
        url = self.base_url.format(company_name)
        r = requests.get(url)
        content = r.content[len(self.yahoo_response_string):-1]
        if r.status_code == 200:
            data = json.loads(content)
            resultset = data.get('ResultSet', None)
            result = resultset.get('Result', None)
            for rinfo in result:
                if rinfo['exchDisp'] in self.stockr_exchanges:
                    return rinfo['symbol']
        else:
            logger.warn('YahooFinance fail: {0}'.format(content))
        return None

    def get_name(self, ticker):
        url = self.base_url.format(ticker)
        r = requests.get(url)
        content = r.content[len(self.yahoo_response_string):-1]
        if r.status_code == 200:
            data = json.loads(content)
            resultset = data.get('ResultSet', None)
            result = resultset.get('Result', None)
            for rinfo in result:
                if rinfo['exchDisp'] in self.stockr_exchanges:
                    return rinfo['name']
        else:
            logger.warn('YahooFinance fail: {0}'.format(content))
        return None


def main(mode, name):
    yf = YahooFinance()
    if mode == 'c':
        print yf.get_ticker(name)
    elif mode == 't':
        print yf.get_name(name)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: c <company name> or t <ticker>'
    else:
        main(sys.argv[1], sys.argv[2])
