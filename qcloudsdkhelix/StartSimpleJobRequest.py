#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartSimpleJobRequest(Request):

	def __init__(self):
		Request.__init__(self, 'helix', 'qcloudcliV1', 'StartSimpleJob', 'helix.api.qcloud.com')

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_secretId(self):
		return self.get_params().get('secretId')

	def set_secretId(self, secretId):
		self.add_param('secretId', secretId)

	def get_secretKey(self):
		return self.get_params().get('secretKey')

	def set_secretKey(self, secretKey):
		self.add_param('secretKey', secretKey)

	def get_desc(self):
		return self.get_params().get('desc')

	def set_desc(self, desc):
		self.add_param('desc', desc)

	def get_timeout(self):
		return self.get_params().get('timeout')

	def set_timeout(self, timeout):
		self.add_param('timeout', timeout)

	def get_imgId(self):
		return self.get_params().get('imgId')

	def set_imgId(self, imgId):
		self.add_param('imgId', imgId)

	def get_cmd(self):
		return self.get_params().get('cmd')

	def set_cmd(self, cmd):
		self.add_param('cmd', cmd)

	def get_instanceType(self):
		return self.get_params().get('instanceType')

	def set_instanceType(self, instanceType):
		self.add_param('instanceType', instanceType)

	def get_rootPassword(self):
		return self.get_params().get('rootPassword')

	def set_rootPassword(self, rootPassword):
		self.add_param('rootPassword', rootPassword)

	def get_dataDiskSize(self):
		return self.get_params().get('dataDiskSize')

	def set_dataDiskSize(self, dataDiskSize):
		self.add_param('dataDiskSize', dataDiskSize)

	def get_network(self):
		return self.get_params().get('network')

	def set_network(self, network):
		self.add_param('network', network)

	def get_extPathMap(self):
		return self.get_params().get('extPathMap')

	def set_extPathMap(self, extPathMap):
		self.add_param('extPathMap', extPathMap)

