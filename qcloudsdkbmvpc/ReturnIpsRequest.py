#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ReturnIpsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bmvpc', 'qcloudcliV1', 'ReturnIps', 'bmvpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_ips(self):
		return self.get_params().get('ips')

	def set_ips(self, ips):
		self.add_param('ips', ips)

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_ips(self):
		return self.get_params().get('ips')

	def set_ips(self, ips):
		self.add_param('ips', ips)

