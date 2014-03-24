##yahoofinance

### Overview
Client to retrieve ticker symbol or full company name
using Yahoo Finance API

### Requirements

    $ pip install requests

### Example Usage

    from yahoofinance import YahooFinance
    yf = YahooFinance()
    print yf.get_ticker('Google')
    ## returns GOOG
    print yf.get_name('Google')
    ## returns Google Inc.

### Meta

Licensed under the MIT license. http://opensource.org/licenses/MIT
