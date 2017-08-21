#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpdatePolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cam', 'qcloudcliV1', 'UpdatePolicy', 'cam.api.qcloud.com')

	def get_policyId(self):
		return self.get_params().get('policyId')

	def set_policyId(self, policyId):
		self.add_param('policyId', policyId)

	def get_policyName(self):
		return self.get_params().get('policyName')

	def set_policyName(self, policyName):
		self.add_param('policyName', policyName)

	def get_policyRemark(self):
		return self.get_params().get('policyRemark')

	def set_policyRemark(self, policyRemark):
		self.add_param('policyRemark', policyRemark)

	def get_policyDocument(self):
		return self.get_params().get('policyDocument')

	def set_policyDocument(self, policyDocument):
		self.add_param('policyDocument', policyDocument)

