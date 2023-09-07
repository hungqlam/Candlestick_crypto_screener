# Candlestick_crypto_screener

## README for Cryptocurrency Pattern Detection Web Application

---

### Description

This repository contains a Flask-based web application designed to detect and analyze candlestick patterns in cryptocurrency price data. Users can select specific candlestick patterns and view their occurrences within the historical OHLCV data of various cryptocurrencies.

### Requirements

- Python 3.x
- Flask
- ccxt (for cryptocurrency exchange interactions)
- pandas
- TA-Lib (for technical analysis)

### How to Run

1. Ensure you have all the required libraries installed.
2. Clone the repository and navigate to the project directory.
3. Run the Flask app using:

```bash
flask run
```

This will start the web server, and the application can be accessed via a web browser.

### File Structure

- `app.py`: The main Flask application script that integrates the pattern detection, data fetching, and web interface.
- `get_price_from_exchange.py`: Contains the functionality to fetch OHLCV data for a given cryptocurrency from a specified exchange.
- `pattern.py`: Provides a dictionary mapping TA-Lib candlestick pattern function names to their descriptive names.

### Features

- **Candlestick Pattern Detection**: Users can select from a wide range of candlestick patterns and view their occurrences in the price data.
- **Cryptocurrency Data Fetching**: The app fetches and processes historical OHLCV data for selected cryptocurrencies using the ccxt library.
- **User-Friendly Interface**: The Flask-based web interface provides an intuitive way to interact with the application.

### Contributions

Feel free to fork this repository and contribute. Pull requests, enhancements, and bug reports are welcome.

---

