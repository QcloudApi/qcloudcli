#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class EnableVpcPeeringConnectionRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'EnableVpcPeeringConnection', 'vpc.api.qcloud.com')

	def get_peeringConnectionId(self):
		return self.get_params().get('peeringConnectionId')

	def set_peeringConnectionId(self, peeringConnectionId):
		self.add_param('peeringConnectionId', peeringConnectionId)

