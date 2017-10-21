#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from urllib.parse import urlencode, urlparse
except ImportError:
    from urllib import urlencode
    from urlparse import urlparse
import copy
import time
import random
import sys
import warnings
import os
warnings.filterwarnings("ignore")

from .sign import Sign
from .userInfo import UserInfo

from qcloudcli import configure
from . import enum
from .base import BaseModule
from .base import BaseMonitorDimension

import socket
try:
    from http.client import HTTPConnection, BadStatusLine, HTTPSConnection
except ImportError:
    from httplib import HTTPConnection, BadStatusLine, HTTPSConnection

class MyHTTPSConnection(HTTPSConnection):
    def __init__(self, host, port=None):
        self.has_proxy = False
        self.request_host = host
        https_proxy = os.environ.get('https_proxy') or os.environ.get('HTTPS_PROXY')
        if https_proxy:
            url = urlparse(https_proxy)
            if not url.hostname:
                url = urlparse('https://' + https_proxy)
            host = url.hostname
            port = url.port
            self.has_proxy = True
        HTTPSConnection.__init__(self, host, port)
        self.request_length = 0

    def send(self, astr):
        HTTPSConnection.send(self, astr)
        self.request_length += len(astr)

    def request(self, method, url, body=None, headers={}):
        self.request_length = 0
        if self.has_proxy:
            self.set_tunnel(self.request_host, 443)
        HTTPSConnection.request(self, method, url, body, headers)


def _fix_params(prefix, params):
    d = {}
    if params is None:
        return d

    if isinstance(params, BaseModule):
        return d

    if not isinstance(params, (tuple, list, dict, BaseMonitorDimension)):
        if isinstance(params, enum.Enum):
            params = params.value
        d[prefix] = params
        return d

    if isinstance(params, (list, tuple)):
        for idx, item in enumerate(params):
            if prefix:
                key = "{0}.{1}".format(prefix, idx)
            else:
                key = "{0}".format(idx)
            d.update(_fix_params(key, item))
        return d

    if isinstance(params, dict):
        for k, v in params.items():
            if prefix:
                key = '{0}.{1}'.format(prefix, k)
            else:
                key = '{0}'.format(k)
            d.update(_fix_params(key, v))
        return d
    raise Exception("fix_param error")


class Request(UserInfo):
    timeout = 10
    version = 'qcloudcliV1'
    def __init__(self, product, version, action_name, requestHost):
        UserInfo.__init__(self, secret_id='123', secret_key='123', method='GET', region_id='gz', auto_retry=True, max_retry_time=3, user_agent=None, port=80)
        #self, secret_id = '123', secret_key = '123', method = 'GET', region_id = 'gz', auto_retry = True, max_retry_time = 3, user_agent = None, port = 80
        self.__requestHost = requestHost
        self.__requestUri = '/v2/index.php'
        self.__params = {}
        self.__product = product
        self.__version = version
        self.api_version = configure.QcloudConfig().getConfig().get(product, '')
        self.__action_name = action_name
        self.__debug = 0
        self.__files = {}
        self.__conn = MyHTTPSConnection(requestHost)

    def add_param(self, k, v):
        if self.__params is None:
           self.__params = {}
        self.__params[k] = v

    def get_params(self):
        return self.__params

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_version(self, version):
        self.__version = version

    def get_version(self):
        return self.__version

    def set_action_name(self, action_name):
        self.__action_name = action_name

    def get_action_name(self):
        return self.__action_name

    def getUrl(self):
        self.checkParams(self.__action_name, self.__params)
        if self.api_version:
            self.__params['Version'] = self.api_version
        self.__params['RequestSource'] = self.__version
        sign = Sign(self.secret_id, self.secret_key)
        self.__params['Signature'] = sign.make(self.__requestHost, self.__requestUri, self.__params, self.request_method)
        params = urlencode(self.__params)

        url = 'https://%s%s' % (self.__requestHost, self.__requestUri)
        if (self.request_method.upper() == 'GET'):
            url += '?' + params
        return url

    def call(self):
        self.checkParams(self.__action_name, self.__params)
        if self.api_version:
            self.__params['Version'] = self.api_version
        self.__params['RequestSource'] = self.__version
        sign = Sign(self.secret_id, self.secret_key)
        self.__params['Signature'] = sign.make(self.__requestHost, self.__requestUri, self.__params, self.request_method)
        params = urlencode(self.__params)

        url = 'https://%s%s' % (self.__requestHost, self.__requestUri)

        if (self.request_method.upper() == 'GET'):
            #req = requests.get(url, params=self.__params, timeout=self.timeout, verify=False)
            req_inter_url = '%s?%s' % (self.__requestUri, params)
            self.__conn.request('GET', req_inter_url, None, {})
            if (self.__debug):
                print('url:', req_inter_url, '\n')
        else:
            #req = requests.post(url, data=self.__params, files=self.__files, timeout=self.timeout, verify=False)
            self.__conn.request('POST', self.__requestUri, params, {'Content-Type':'application/x-www-form-urlencoded'})
            if (self.__debug):
                print('url:', url, '\n')

        self.__conn.sock.settimeout(self.timeout)
        self.__conn.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            http_resp = self.__conn.getresponse()
        except BadStatusLine:
            #open another connection when keep-alive timeout
            #httplib will not handle keep-alive timeout, so we must handle it ourself
            self.__conn.close()
            self.__conn.request('POST', self.__requestUri, params, {'Content-Type':'application/x-www-form-urlencoded'})
            self.__conn.sock.settimeout(self.timeout)
            self.__conn.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            http_resp = self.__conn.getresponse()

        if http_resp.status != 200:
            raise Exception('%s Http Response Status Error\nHeaders:%s\nBody:%s' % (http_resp.status, http_resp.getheaders(), http_resp.read()))

        result = http_resp.read()
        self.__conn.close()
        return result

    def checkParams(self, action, params):
        params_list_format = self.fix_params(params)
        self.__params = copy.deepcopy(params_list_format)
        self.__params['Action'] = action
        if (('Region' in self.__params) != True):
            self.__params['Region'] = self.region_id

        if (('SecretId' in self.__params) != True):
            self.__params['SecretId'] = self.secret_id

        if (('Nonce' in self.__params) != True):
            self.__params['Nonce'] = random.randint(1, sys.maxsize)

        if (('Timestamp' in self.__params) != True):
            self.__params['Timestamp'] = int(time.time())

        return self.__params

    def fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        return _fix_params(None, params)
