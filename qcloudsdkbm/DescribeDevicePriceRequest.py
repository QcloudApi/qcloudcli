#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeDevicePriceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bm', 'qcloudcliV1', 'DescribeDevicePrice', 'bm.api.qcloud.com')

	def get_instanceIds(self):
		return self.get_params().get('instanceIds')

	def set_instanceIds(self, instanceIds):
		self.add_param('instanceIds', instanceIds)

	def get_timeUnit(self):
		return self.get_params().get('timeUnit')

	def set_timeUnit(self, timeUnit):
		self.add_param('timeUnit', timeUnit)

	def get_timeSpan(self):
		return self.get_params().get('timeSpan')

	def set_timeSpan(self, timeSpan):
		self.add_param('timeSpan', timeSpan)

