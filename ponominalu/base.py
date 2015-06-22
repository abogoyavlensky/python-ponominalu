# -*- coding: utf-8 -*-
"""
    ponominalu.base
    ~~~~~~~~~~~~~~~

    Basic functional for api.

    :copyright: (c) 2015 by Rambler&Co.
"""

import os
import time
import requests


class BaseAPI(object):
    host = ''
    key_param_name = 'session'

    def __init__(self, key=None):
        self.key = key

    def request(self, path, allowed_params=None, allowed_data=None,
                method='get', params=None, data=None):
        """
        Method for making method for api.
        Example of usage:
            def project_list(self, **kwargs):
                return self.request(
                    path='/project/list',
                    **kwargs
                )
        """
        params, data = params or {}, data or {}
        allowed_params = allowed_params or []
        allowed_data = allowed_data or []

        for key in params.keys():
            if key not in allowed_params:
                raise ValueError(
                    'Param {0} was not found in allowed params.'
                    .format(key)
                )

        for key in data.keys():
            if key not in allowed_data:
                raise ValueError(
                    'Param {0} was not found in allowed params.'
                    .format(key)
                )

        params.update({self.key_param_name: self.key})
        url = os.path.join(self.host, path)
        try:
            response = requests.request(method, url, params=params, data=data)
        except Exception as e:
            raise BaseAPIError(404, e, 'requestsFailed')
        else:
            try:
                response = response.json()
            except Exception as e:
                pass

        return response

    def perform_request(self, method, params, to_wait=True):
        result = getattr(self, method)(params=params)
        if to_wait:
            time.sleep(0.2)
        return result


class BaseAPIError(Exception):
    """API Client error"""

    def __init__(self, code, message, error_code):
        self.code = code
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return self.message
