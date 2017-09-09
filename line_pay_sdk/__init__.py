# -*- coding: utf-8 -*-
import json
import requests

from optionaldict import optionaldict
from .base import BaseLINEPayAPI
from .exceptions import LINEPayException

from .payment import LINEPayPayment

"""
A LINE Pay SDK
"""

class LINEPay(object):
    """
    LINE Pay client
    """
    
    API_BASE_URL = 'https://api-pay.line.me'

    def __init__(self, channel_id, channel_secret_key):
        self._http = requests.Session()
        self.channel_id = channel_id
        self.channel_secret_key = channel_secret_key

    def _del_none(self, data):
        for key, value in list(data.items()):
            if value is None:
                del data[key]
            elif isinstance(value, dict):
                self._del_none(value)

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=url_or_endpoint
            )
        else:
            url = url_or_endpoint

        if isinstance(kwargs.get('data', ''), dict):
            data = optionaldict(kwargs['data'])
            self._del_none(data)
            # body = json.dumps(data)
            # # body = body.encode('utf-8')
            kwargs['data'] = json.dumps(data)
        kwargs['headers'] = {
            'X-LINE-ChannelId': self.channel_id,
            'X-LINE-ChannelSecret': self.channel_secret_key,
            'Content-Type': 'application/json',
        }

        res = self._http.request(
            method=method,
            url=url,
            verify=False,
            **kwargs
        )
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            raise LINEPayException(
                None,
                None,
                client=self,
                request=reqe.request,
                response=reqe.response
            )

        return self._handle_result(res)

    def get(self, url, **kwargs):
        return self._request(
            method='get',
            url_or_endpoint=url,
            **kwargs
        )

    def post(self, url, **kwargs):
        return self._request(
            method='post',
            url_or_endpoint=url,
            **kwargs
        )

    def _handle_result(self, res):
        print(res.text)
        res.encoding = 'utf-8'
        data = res.json()

        return_code = data['returnCode']
        return_message = data['returnMessage']
        error_detail_map = data.get('errorDetailMap')
        if return_code != '0000':
            raise LINEPayException(
                return_code,
                return_message,
                error_detail_map,
                client=self,
                request=res.request,
                response=res
            )
        return data
