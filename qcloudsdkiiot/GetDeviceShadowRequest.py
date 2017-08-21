#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetDeviceShadowRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'GetDeviceShadow', 'iiot.api.qcloud.com')

	def get_deviceName(self):
		return self.get_params().get('deviceName')

	def set_deviceName(self, deviceName):
		self.add_param('deviceName', deviceName)

