#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpgradeDBInstanceEngineVersionV3Request(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'UpgradeDBInstanceEngineVersionV3', 'cdb.api.qcloud.com')

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)

	def get_engineVersion(self):
		return self.get_params().get('engineVersion')

	def set_engineVersion(self, engineVersion):
		self.add_param('engineVersion', engineVersion)

	def get_waitSwitch(self):
		return self.get_params().get('waitSwitch')

	def set_waitSwitch(self, waitSwitch):
		self.add_param('waitSwitch', waitSwitch)

