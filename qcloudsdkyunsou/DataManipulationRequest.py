#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DataManipulationRequest(Request):

	def __init__(self):
		Request.__init__(self, 'yunsou', 'qcloudcliV1', 'DataManipulation', 'yunsou.api.qcloud.com')

	def get_appId(self):
		return self.get_params().get('appId')

	def set_appId(self, appId):
		self.add_param('appId', appId)

	def get_op_type(self):
		return self.get_params().get('op_type')

	def set_op_type(self, op_type):
		self.add_param('op_type', op_type)

	def get_contents(self):
		return self.get_params().get('contents')

	def set_contents(self, contents):
		self.add_param('contents', contents)
