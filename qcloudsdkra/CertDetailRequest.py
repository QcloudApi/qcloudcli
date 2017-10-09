#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CertDetailRequest(Request):

	def __init__(self):
		Request.__init__(self, 'ra', 'qcloudcliV1', 'CertDetail', 'ra.api.qcloud.com')

	def get_module(self):
		return self.get_params().get('module')

	def set_module(self, module):
		self.add_param('module', module)

	def get_operation(self):
		return self.get_params().get('operation')

	def set_operation(self, operation):
		self.add_param('operation', operation)

	def get_certSn(self):
		return self.get_params().get('certSn')

	def set_certSn(self, certSn):
		self.add_param('certSn', certSn)

	def get_certDn(self):
		return self.get_params().get('certDn')

	def set_certDn(self, certDn):
		self.add_param('certDn', certDn)

