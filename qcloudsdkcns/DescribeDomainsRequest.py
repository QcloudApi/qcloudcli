#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeDomainsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cns', 'qcloudcliV1', 'DescribeDomains', 'cns.api.qcloud.com')

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)
	
	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)


