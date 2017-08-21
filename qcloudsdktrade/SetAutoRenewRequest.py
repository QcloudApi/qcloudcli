#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class SetAutoRenewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'SetAutoRenew', 'trade.api.qcloud.com')

	def get_instanceType(self):
		return self.get_params().get('instanceType')

	def set_instanceType(self, instanceType):
		self.add_param('instanceType', instanceType)
		
	def get_instanceIds(self):
		return self.get_params().get('instanceIds')

	def set_instanceIds(self, instanceIds):
		self.add_param('instanceIds', instanceIds)
		
	def get_autoRenew(self):
		return self.get_params().get('autoRenew')

	def set_autoRenew(self, autoRenew):
		self.add_param('autoRenew', autoRenew)