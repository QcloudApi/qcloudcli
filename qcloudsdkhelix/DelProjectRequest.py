#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DelProjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'helix', 'qcloudcliV1', 'DelProject', 'helix.api.qcloud.com')

	def get_secretId(self):
		return self.get_params().get('secretId')

	def set_secretId(self, secretId):
		self.add_param('secretId', secretId)

	def get_secretKey(self):
		return self.get_params().get('secretKey')

	def set_secretKey(self, secretKey):
		self.add_param('secretKey', secretKey)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

