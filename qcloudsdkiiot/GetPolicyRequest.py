#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'GetPolicy', 'iiot.api.qcloud.com')

	def get_policyId(self):
		return self.get_params().get('policyId')

	def set_policyId(self, policyId):
		self.add_param('policyId', policyId)

	def get_policyName(self):
		return self.get_params().get('policyName')

	def set_policyName(self, policyName):
		self.add_param('policyName', policyName)

