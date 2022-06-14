# CurrencyAPI Python Client #

CurrencyAPI Python Client is the official Python Wrapper around the CurrencyAPI [API](https://currencyapi.com/).

## Installation

Install from pip:
````sh
pip install currencyapicom
````

Install from code:
````sh
pip install git+https://github.com/everapihq/currencyapi-python.git
````

## Usage

All curencyapi API requests are made using the `Client` class. This class must be initialized with your API access key string. [Where is my API access key?](https://app.currencyapi.com/dashboard)

In your Python application, import `currencyapicom` and pass authentication information to initialize it:

````python
import currencyapicom
client = currencyapicom.Client('API_KEY')
````

### Retrieve Status

```python

print(client.status())

```

### Retrieve Currencies
[https://currencyapi.com/docs/currencies](https://currencyapi.com/docs/currencies)
```python

result = client.currencies(currencies=['EUR', 'CAD'])
print(result)

```

### Retrieve Latest Exchange Rates
[https://currencyapi.com/docs/latest](https://currencyapi.com/docs/latest)

```python

result = client.latest()
print(result)

```

### Retrieve Historical Exchange Rates
[https://currencyapi.com/docs/historical](https://currencyapi.com/docs/historical)

```python

result = client.historical('2022-02-02')
print(result)

```

### Retrieve Historical Range Exchange Rates
[https://currencyapi.com/docs/range](https://currencyapi.com/docs/range)

```python

result = client.range('2022-02-02', '2022-02-04')
print(result)

```

### Retrieve Converted Exchange Rates
[https://currencyapi.com/docs/convert](https://currencyapi.com/docs/convert)

```python

result = client.convert(1234)
print(result)

```


### Contact us
Any feedback? Please feel free to [contact our team](mailto:office@everapi.com).
