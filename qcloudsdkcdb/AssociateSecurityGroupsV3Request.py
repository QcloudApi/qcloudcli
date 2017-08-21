#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class AssociateSecurityGroupsV3Request(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'AssociateSecurityGroupsV3', 'cdb.api.qcloud.com')

	def get_securityGroupId(self):
		return self.get_params().get('securityGroupId')

	def set_securityGroupId(self, securityGroupId):
		self.add_param('securityGroupId', securityGroupId)

	def get_instanceIds(self):
		return self.get_params().get('instanceIds')

	def set_instanceIds(self, instanceIds):
		self.add_param('instanceIds', instanceIds)

