#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeDealsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'DescribeDeals', 'trade.api.qcloud.com')

	def get_dealIds(self):
		return self.get_params().get('dealIds')

	def set_dealIds(self, dealIds):
		self.add_param('dealIds', dealIds)
		
	def get_startTime(self):
		return self.get_params().get('startTime')

	def set_startTime(self, startTime):
		self.add_param('startTime', startTime)

	def get_endTime(self):
		return self.get_params().get('endTime')

	def set_endTime(self, endTime):
		self.add_param('endTime', endTime)
		
	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)
		
	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)
