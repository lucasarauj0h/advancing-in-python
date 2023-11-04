import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

end_date = datetime.now().strftime('%Y-%m-%d')
print(end_date)

# codigo banco do brasil
bb = yf.Ticker('BBAS3.SA')
data_bb = bb.history(
    start='2020-07-20',
    end= end_date
)

data_bb['Close'].plot()
plt.savefig('bb_preco.png')