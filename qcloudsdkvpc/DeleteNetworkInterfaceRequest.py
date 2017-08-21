#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteNetworkInterfaceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'DeleteNetworkInterface', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_networkInterfaceId(self):
		return self.get_params().get('networkInterfaceId')

	def set_networkInterfaceId(self, networkInterfaceId):
		self.add_param('networkInterfaceId', networkInterfaceId)

