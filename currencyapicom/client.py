import currencyapicom
import requests
import json
import requests.exceptions
import logging
import currencyapicom.exceptions


class Client(object):
    api_key = None
    headers = {}
    debug = False

    def __init__(self, api_key=None):

        self.headers['User-Agent'] = 'CurrencyAPI_Python'
        self.headers['Accept'] = 'application/json'
        self.headers['Content-Type'] = 'application/json'

        if api_key:
            self.api_key = api_key

        self.api_base = currencyapicom.api_base

        if currencyapicom.debug:
            self.debug = True
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(message)s')

    def status(self):
        return self._request('/status')

    def currencies(self, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/currencies', params={
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def latest(self, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/latest', params={
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def historical(self, date, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/historical', params={
            'date': date,
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def range(self, datetime_start, datetime_end, accuracy=None, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/range', params={
            'datetime_start': datetime_start,
            'datetime_end': datetime_end,
            'accuracy': accuracy,
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def convert(self, value, date=None, base_currency=None, currencies=[]):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        return self._request('/convert', params={
            'value': value,
            'date': date,
            'base_currency': base_currency,
            'currencies': self._list_to_comma_seperated(currencies)
        })

    def _list_to_comma_seperated(self, lst):
        return ','.join(lst)

    def _request(self, url, method="GET", params=dict(), data=None,
                 return_type=None):
        url = self.api_base + url

        if self.api_key:
            self.headers['apikey'] = self.api_key

        try:
            if method in ["GET", "DELETE"]:
                response = requests.request(
                    method, url, headers=self.headers, params=params)

            elif method == "POST":
                if self.debug:
                    logging.debug(data)
                response = requests.request(
                    method, url, headers=self.headers, params=params, json=data)

            else:
                raise Exception("Method not supported")

            if response.status_code == 429:
                if 'x-ratelimit-remaining-quota-month' in response.headers:
                    quota = response.headers['x-ratelimit-remaining-quota-month']
                    if int(quota) <= 0:
                        raise currencyapicom.exceptions.QuotaExceeded()
                    raise currencyapicom.exceptions.RateLimitExceeded()

            elif response.status_code == 403:
                raise currencyapicom.exceptions.NotAllowed()

            response_obj = json.loads(response.text)

            if self.debug:
                logging.debug(response_obj)

            if "errors" in response_obj:
                raise currencyapicom.exceptions.ApiError("API returned errors:", response_obj['errors'])

            return response_obj

        except requests.exceptions.RequestException:
            raise
