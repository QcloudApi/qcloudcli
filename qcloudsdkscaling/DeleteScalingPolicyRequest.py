#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteScalingPolicyRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scaling', 'qcloudcliV1', 'DeleteScalingPolicy', 'scaling.api.qcloud.com')

	def get_scalingGroupId(self):
		return self.get_params().get('scalingGroupId')

	def set_scalingGroupId(self, scalingGroupId):
		self.add_param('scalingGroupId', scalingGroupId)

	def get_scalingPolicyId(self):
		return self.get_params().get('scalingPolicyId')

	def set_scalingPolicyId(self, scalingPolicyId):
		self.add_param('scalingPolicyId', scalingPolicyId)

