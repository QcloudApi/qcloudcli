#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteScalingConfigurationRequest(Request):

	def __init__(self):
		Request.__init__(self, 'scaling', 'qcloudcliV1', 'DeleteScalingConfiguration', 'scaling.api.qcloud.com')

	def get_scalingConfigurationId(self):
		return self.get_params().get('scalingConfigurationId')

	def set_scalingConfigurationId(self, scalingConfigurationId):
		self.add_param('scalingConfigurationId', scalingConfigurationId)

