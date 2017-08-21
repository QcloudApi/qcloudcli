#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DetachRolesPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cam', 'qcloudcliV1', 'DetachRolesPolicy', 'cam.api.qcloud.com')

	def get_roleId(self):
		return self.get_params().get('roleId')

	def set_roleId(self, roleId):
		self.add_param('roleId', roleId)

