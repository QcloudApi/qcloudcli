#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeBmLoadBalancersTaskResultRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bmlb', 'qcloudcliV1', 'DescribeBmLoadBalancersTaskResult', 'bmlb.api.qcloud.com')

	def get_requestId(self):
		return self.get_params().get('requestId')

	def set_requestId(self, requestId):
		self.add_param('requestId', requestId)

	def get_requestId(self):
		return self.get_params().get('requestId')

	def set_requestId(self, requestId):
		self.add_param('requestId', requestId)

