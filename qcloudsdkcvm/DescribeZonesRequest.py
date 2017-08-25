#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeZonesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cvm', 'qcloudcliV1', 'DescribeZones', 'cvm.api.qcloud.com')

	def set_Version(self, Version):
		self.add_param('Version', Version)
