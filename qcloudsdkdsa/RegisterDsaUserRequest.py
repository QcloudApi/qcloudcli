#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RegisterDsaUserRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dsa', 'qcloudcliV1', 'RegisterDsaUser', 'dsa.api.qcloud.com')

	def get_payType(self):
		return self.get_params().get('payType')

	def set_payType(self, payType):
		self.add_param('payType', payType)

	def get_billingType(self):
		return self.get_params().get('billingType')

	def set_billingType(self, billingType):
		self.add_param('billingType', billingType)

