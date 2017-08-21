#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RefreshCdnUrlRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'RefreshCdnUrl', 'cdn.api.qcloud.com')

	def get_urls(self):
		return self.get_params().get('urls')

	def set_urls(self, urls):
		self.add_param('urls', urls)

