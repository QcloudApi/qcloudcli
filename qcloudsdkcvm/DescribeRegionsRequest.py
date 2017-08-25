#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeRegionsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cvm', 'qcloudcliV1', 'DescribeRegions', 'cvm.api.qcloud.com')

	def set_Version(self, Version):
		self.add_param('Version', Version)
