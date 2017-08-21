#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyVpcAttributeRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'ModifyVpcAttribute', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_vpcName(self):
		return self.get_params().get('vpcName')

	def set_vpcName(self, vpcName):
		self.add_param('vpcName', vpcName)

	def get_isMulticast(self):
		return self.get_params().get('isMulticast')

	def set_isMulticast(self, isMulticast):
		self.add_param('isMulticast', isMulticast)

