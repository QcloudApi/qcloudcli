#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribePoincyInfoByInstanceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'DescribePoincyInfoByInstance', 'monitor.api.qcloud.com')

	def get_viewName(self):
		return self.get_params().get('viewName')

	def set_viewName(self, viewName):
		self.add_param('viewName', viewName)

	def get_dimension(self):
		return self.get_params().get('dimension')

	def set_dimension(self, dimension):
		self.add_param('dimension', dimension)

