#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetFunctionRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scf', 'qcloudcliV1', 'GetFunction', 'scf.api.qcloud.com')

	def get_functionName(self):
		return self.get_params().get('functionName')

	def set_functionName(self, functionName):
		self.add_param('functionName', functionName)

	def get_code(self):
		return self.get_params().get('code')

	def set_code(self, code):
		self.add_param('code', code)

