#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UnassignPrivateIpAddressesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'UnassignPrivateIpAddresses', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_networkInterfaceId(self):
		return self.get_params().get('networkInterfaceId')

	def set_networkInterfaceId(self, networkInterfaceId):
		self.add_param('networkInterfaceId', networkInterfaceId)

	def get_privateIpAddress(self):
		return self.get_params().get('privateIpAddress')

	def set_privateIpAddress(self, privateIpAddress):
		self.add_param('privateIpAddress', privateIpAddress)

