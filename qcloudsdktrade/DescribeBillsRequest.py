#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeBillsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'DescribeBills', 'trade.api.qcloud.com')

	def get_startDate(self):
		return self.get_params().get('startDate')

	def set_startDate(self, startDate):
		self.add_param('startDate', startDate)
		
	def get_endDate(self):
		return self.get_params().get('endDate')

	def set_endDate(self, endDate):
		self.add_param('endDate', endDate)

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)
		
	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)
		
	def get_orderType(self):
		return self.get_params().get('orderType')

	def set_orderType(self, orderType):
		self.add_param('orderType', orderType)