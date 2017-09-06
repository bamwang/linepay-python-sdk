# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import six
from .utils import to_binary, to_text

class LINEPayException(Exception):
    """Base exception for wechatpy"""

    def __init__(self, return_code, return_message, error_detail_map=None, client=None,
                 request=None, response=None):
        """
        :param return_code: Error code
        :param return_message: Error message
        """
        self.return_code = return_code
        self.return_message = return_message
        self.error_detail_map = error_detail_map
        self.client = client
        self.request = request
        self.response = response

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}, detail: {detail}'.format(
            code=self.return_code,
            msg=self.return_message,
            detail=self.error_detail_map
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.return_code,
            msg=self.return_message
        )
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)
