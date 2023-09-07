from flask import Flask,render_template,request,redirect
from pattern import patterns
from get_price_from_exchange import getprices
from flask import Flask, jsonify
import os
import pandas as pd
import re
import talib
import csv
app = Flask(__name__)
# Global variables to track progress
total_currencies = 0
processed_currencies = 0
@app.route('/')
def index():
    pattern=request.args.get('pattern',None)
    crypto={}
    with open('datasets/currencies.csv') as f:
        reader=csv.reader(f)
        for row in reader:
            key=row[0].replace('/','')
            crypto[key] = {'currency':row[1]}
        #print(crypto)

    if pattern:
        datafiles=os.listdir('datasets/daily')
        for filename in datafiles:
            df=pd.read_csv('datasets/daily/{}'.format(filename))
            pattern_function=getattr(talib,pattern)
            symb= filename.split('.')[0]
            try:
                result = pattern_function(df['Open'],df['High'],df['Low'],df['Close'])
                #print(result)
                last = result.tail(1).values[0]
                if last >0:
                    crypto[symb][pattern] ='bullish'
                elif last <0:
                    crypto[symb][pattern] ='bearish'
                else:
                    crypto[symb][pattern] =None
            except:
                pass

    return render_template('index.html', patterns=patterns, crypto=crypto,current_pattern=pattern)


@app.route('/progress')
def progress():
    # Return the current progress as a percentage
    if total_currencies == 0:
        return jsonify(progress=0)
    else:
        return jsonify(progress=100 * processed_currencies / total_currencies)
    

@app.route('/snapshot')
def snapshot():
    global total_currencies
    global processed_currencies

    exchange='binance' #put name of the exchange 
    directory = 'datasets/daily'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('datasets/currencies.csv') as f:
        currencies = f.read().splitlines()
        total_currencies = len(currencies)
        processed_currencies = 0
        for currency in currencies:
            symbol = currency.split(',')[0]
            df=pd.DataFrame(getprices(exchange,symbol))
            # Keep only alphanumeric characters
            symbol = re.sub(r'\W+', '', symbol)
            df.to_csv(os.path.join(directory, '{}.csv'.format(symbol)))
            processed_currencies += 1

    return redirect('/')
