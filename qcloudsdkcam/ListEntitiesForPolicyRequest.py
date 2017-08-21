#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ListEntitiesForPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cam', 'qcloudcliV1', 'ListEntitiesForPolicy', 'cam.api.qcloud.com')

	def get_policyId(self):
		return self.get_params().get('policyId')

	def set_policyId(self, policyId):
		self.add_param('policyId', policyId)

