from yahooquery import Ticker

symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

def get_values_actions():
    faang = Ticker(symbols)

    actions = []
    for symbol in symbols:
        open = faang.summary_detail[symbol]['open']
        close = faang.summary_detail[symbol]['previousClose']

        perc = 0
        if close >= open:
            perc = (close / open - 1) * 100
        else:
            perc = 1 - open / close
        actions.append({
            'name': symbol.upper(),
            'perc': round(perc, 4)
        })
    return actions