#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class InquiryLBPriceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'InquiryLBPrice', 'lb.api.qcloud.com')

	def get_loadBalancerType(self):
		return self.get_params().get('loadBalancerType')

	def set_loadBalancerType(self, loadBalancerType):
		self.add_param('loadBalancerType', loadBalancerType)

	def get_timeUnit(self):
		return self.get_params().get('timeUnit')

	def set_timeUnit(self, timeUnit):
		self.add_param('timeUnit', timeUnit)

