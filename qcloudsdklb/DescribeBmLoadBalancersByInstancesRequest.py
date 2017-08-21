#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeBmLoadBalancersByInstancesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'DescribeBmLoadBalancersByInstances', 'lb.api.qcloud.com')

	def get_backendInstanceIds(self):
		return self.get_params().get('backendInstanceIds')

	def set_backendInstanceIds(self, backendInstanceIds):
		self.add_param('backendInstanceIds', backendInstanceIds)

	def get_backendInstanceName(self):
		return self.get_params().get('backendInstanceName')

	def set_backendInstanceName(self, backendInstanceName):
		self.add_param('backendInstanceName', backendInstanceName)

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

