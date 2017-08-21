#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeProductRegionListRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'DescribeProductRegionList', 'trade.api.qcloud.com')

	def get_instanceType(self):
		return self.get_params().get('instanceType')

	def set_instanceType(self, instanceType):
		self.add_param('instanceType', instanceType)