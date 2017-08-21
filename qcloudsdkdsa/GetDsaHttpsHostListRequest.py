#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetDsaHttpsHostListRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dsa', 'qcloudcliV1', 'GetDsaHttpsHostList', 'dsa.api.qcloud.com')

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_length(self):
		return self.get_params().get('length')

	def set_length(self, length):
		self.add_param('length', length)

