#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetCdbInstanceNumByVpcSubnetIdRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'GetCdbInstanceNumByVpcSubnetId', 'cdb.api.qcloud.com')

	def get_vpcId(self):
		return self.get_params().get('vpcId')

	def set_vpcId(self, vpcId):
		self.add_param('vpcId', vpcId)

	def get_subnetIds(self):
		return self.get_params().get('subnetIds')

	def set_subnetIds(self, subnetIds):
		self.add_param('subnetIds', subnetIds)

