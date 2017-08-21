#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeSSLVpnDomainRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'DescribeSSLVpnDomain', 'vpc.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_sslVpnId(self):
		return self.get_params().get('sslVpnId')

	def set_sslVpnId(self, sslVpnId):
		self.add_param('sslVpnId', sslVpnId)

