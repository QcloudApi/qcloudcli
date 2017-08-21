#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeUserGroupRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'DescribeUserGroup', 'trade.api.qcloud.com')

	def get_groupIds(self):
		return self.get_params().get('groupIds')

	def set_groupIds(self, groupIds):
		self.add_param('groupIds', groupIds)
		