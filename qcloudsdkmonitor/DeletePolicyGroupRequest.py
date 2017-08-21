#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeletePolicyGroupRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'DeletePolicyGroup', 'monitor.api.qcloud.com')

	def get_groupId(self):
		return self.get_params().get('groupId')

	def set_groupId(self, groupId):
		self.add_param('groupId', groupId)

