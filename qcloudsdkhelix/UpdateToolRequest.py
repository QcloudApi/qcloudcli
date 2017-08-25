#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpdateToolRequest(Request):

	def __init__(self):
		Request.__init__(self, 'helix', 'qcloudcliV1', 'UpdateTool', 'helix.api.qcloud.com')

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_uin(self):
		return self.get_params().get('uin')

	def set_uin(self, uin):
		self.add_param('uin', uin)

	def get_toolId(self):
		return self.get_params().get('toolId')

	def set_toolId(self, toolId):
		self.add_param('toolId', toolId)

	def get_toolVer(self):
		return self.get_params().get('toolVer')

	def set_toolVer(self, toolVer):
		self.add_param('toolVer', toolVer)

	def get_tool(self):
		return self.get_params().get('tool')

	def set_tool(self, tool):
		self.add_param('tool', tool)

