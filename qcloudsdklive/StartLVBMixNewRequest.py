#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartLVBMixNewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'StartLVBMixNew', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

	def get_mixInfoList(self):
		return self.get_params().get('mixInfoList')

	def set_mixInfoList(self, mixInfoList):
		self.add_param('mixInfoList', mixInfoList)

	def get_width(self):
		return self.get_params().get('width')

	def set_width(self, width):
		self.add_param('width', width)

	def get_height(self):
		return self.get_params().get('height')

	def set_height(self, height):
		self.add_param('height', height)

