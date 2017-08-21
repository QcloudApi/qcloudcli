#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateNetworkAclRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'CreateNetworkAcl', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_networkAclName(self):
		return self.get_params().get('networkAclName')

	def set_networkAclName(self, networkAclName):
		self.add_param('networkAclName', networkAclName)

