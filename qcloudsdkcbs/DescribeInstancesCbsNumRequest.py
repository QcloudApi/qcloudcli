#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeInstancesCbsNumRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cbs', 'qcloudcliV1', 'DescribeInstancesCbsNum', 'cbs.api.qcloud.com')

	def get_uInstanceIds(self):
		return self.get_params().get('uInstanceIds')

	def set_uInstanceIds(self, uInstanceIds):
		self.add_param('uInstanceIds', uInstanceIds)

