#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ResizeInstanceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cvm', 'qcloudcliV1', 'ResizeInstance', 'cvm.api.qcloud.com')

	def get_cpu(self):
		return self.get_params().get('cpu')

	def set_cpu(self, cpu):
		self.add_param('cpu', cpu)

	def get_mem(self):
		return self.get_params().get('mem')

	def set_mem(self, mem):
		self.add_param('mem', mem)

	def get_storageSize(self):
		return self.get_params().get('storageSize')

	def set_storageSize(self, storageSize):
		self.add_param('storageSize', storageSize)
		
	def get_storageType(self):
		return self.get_params().get('storageType')

	def set_storageType(self, storageType):
		self.add_param('storageType', storageType)

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)
		
	def get_bandwidth(self):
		return self.get_params().get('bandwidth')

	def set_bandwidth(self, bandwidth):
		self.add_param('bandwidth', bandwidth)
		
	def get_bandwidthUpgradeStartTime(self):
		return self.get_params().get('bandwidthUpgradeStartTime')

	def set_bandwidthUpgradeStartTime(self, bandwidthUpgradeStartTime):
		self.add_param('bandwidthUpgradeStartTime', bandwidthUpgradeStartTime)
		
	def get_bandwidthUpgradeEndTime(self):
		return self.get_params().get('bandwidthUpgradeEndTime')

	def set_bandwidthUpgradeEndTime(self, bandwidthUpgradeEndTime):
		self.add_param('bandwidthUpgradeEndTime', bandwidthUpgradeEndTime)

