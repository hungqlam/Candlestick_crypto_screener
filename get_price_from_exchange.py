import ccxt
import pandas as pd



def getprices(exchange,symbol):
    inst=getattr(ccxt,exchange)()
    df=pd.DataFrame(inst.fetchOHLCV(symbol,'1d'))
    df.columns=['Time','Open','High','Low','Close','Volume']
    df.set_index('Time',inplace=True)
    df.index=pd.to_datetime(df.index,unit='ms')
    df = df.astype(float)
    return df


