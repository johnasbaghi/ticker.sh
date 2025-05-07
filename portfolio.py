import yfinance as yf
from tabulate import tabulate
from simple_colors import red, green
from datetime import datetime

SYMBOLS = ["VOO", "SPY", "VT", "QQQ", "SCHD", "VGK", "XLE", "VB", "VTSAX", "VTI", "MKL", "RKLB", "CNX", "CLF", "HCC", "ADM", "ITA", "IAT", "BAM", "BN", "EWZ", "GLD", "BTC-USD", "CL=F", "GC=F", "SI=F", "ZIM", "TSLA", "IBIT", "FBTC", "MSTR", "IDGT"]

HEADERS=['Symbol', 'Price', '$ Change', '% Change']


def get_current_date_and_time():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def round_to_two_decimals(number):
  """Rounds a number to two decimal places and returns a string representation,
  including trailing zeros.
  """
  return "{:.2f}".format(number)

rows = []
for sym in SYMBOLS:
    dat = yf.Ticker(sym)
    current_price = dat.info['regularMarketPrice']
    previous_close = dat.info['previousClose']
    price_change = round(current_price - previous_close, 2)
    percent_change = round((current_price - previous_close) / previous_close * 100, 2)
    
    row = [sym, round_to_two_decimals(current_price),
           round_to_two_decimals(price_change),
           round_to_two_decimals(percent_change)]

    row = [red(x) for x in row] if price_change < 0 else [green(x) for x in row]

    rows.append(row)


print(get_current_date_and_time())
print(tabulate(rows, HEADERS, disable_numparse=True, colalign=("left", "right", "right", "right")))
