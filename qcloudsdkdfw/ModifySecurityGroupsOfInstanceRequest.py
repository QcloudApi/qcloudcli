#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifySecurityGroupsOfInstanceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dfw', 'qcloudcliV1', 'ModifySecurityGroupsOfInstance', 'dfw.api.qcloud.com')

	def get_instanceSet(self):
		return self.get_params().get('instanceSet')

	def set_instanceSet(self, instanceSet):
		self.add_param('instanceSet', instanceSet)

