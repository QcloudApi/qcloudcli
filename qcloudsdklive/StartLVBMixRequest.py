#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartLVBMixRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'StartLVBMix', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

	def get_mixType(self):
		return self.get_params().get('mixType')

	def set_mixType(self, mixType):
		self.add_param('mixType', mixType)

	def get_mixInfoList(self):
		return self.get_params().get('mixInfoList')

	def set_mixInfoList(self, mixInfoList):
		self.add_param('mixInfoList', mixInfoList)

