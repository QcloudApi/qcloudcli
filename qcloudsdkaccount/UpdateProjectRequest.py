#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpdateProjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'account', 'qcloudcliV1', 'UpdateProject', 'account.api.qcloud.com')

	def get_projectName(self):
		return self.get_params().get('projectName')

	def set_projectName(self, projectName):
		self.add_param('projectName', projectName)

	def get_projectDesc(self):
		return self.get_params().get('projectDesc')

	def set_projectDesc(self, projectDesc):
		self.add_param('projectDesc', projectDesc)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_name(self):
		return self.get_params().get('name')

	def set_name(self, name):
		self.add_param('name', name)

	def get_desc(self):
		return self.get_params().get('desc')

	def set_desc(self, desc):
		self.add_param('desc', desc)

