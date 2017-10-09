#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreatePolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'CreatePolicy', 'iiot.api.qcloud.com')

	def get_policyName(self):
		return self.get_params().get('policyName')

	def set_policyName(self, policyName):
		self.add_param('policyName', policyName)

	def get_policyDocument(self):
		return self.get_params().get('policyDocument')

	def set_policyDocument(self, policyDocument):
		self.add_param('policyDocument', policyDocument)

	def get_policyName(self):
		return self.get_params().get('policyName')

	def set_policyName(self, policyName):
		self.add_param('policyName', policyName)

	def get_policyDocument(self):
		return self.get_params().get('policyDocument')

	def set_policyDocument(self, policyDocument):
		self.add_param('policyDocument', policyDocument)

