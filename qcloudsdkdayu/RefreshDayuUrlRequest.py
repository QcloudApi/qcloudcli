#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RefreshDayuUrlRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dayu', 'qcloudcliV1', 'RefreshDayuUrl', 'dayu.api.qcloud.com')

	def get_urls(self):
		return self.get_params().get('urls')

	def set_urls(self, urls):
		self.add_param('urls', urls)

	def get_dirs(self):
		return self.get_params().get('dirs')

	def set_dirs(self, dirs):
		self.add_param('dirs', dirs)

