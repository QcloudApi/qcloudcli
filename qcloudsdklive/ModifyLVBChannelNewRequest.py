#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyLVBChannelNewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'ModifyLVBChannelNew', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

	def get_channelName(self):
		return self.get_params().get('channelName')

	def set_channelName(self, channelName):
		self.add_param('channelName', channelName)

	def get_channelDescribe(self):
		return self.get_params().get('channelDescribe')

	def set_channelDescribe(self, channelDescribe):
		self.add_param('channelDescribe', channelDescribe)

	def get_outputSourceType(self):
		return self.get_params().get('outputSourceType')

	def set_outputSourceType(self, outputSourceType):
		self.add_param('outputSourceType', outputSourceType)

	def get_outputRate(self):
		return self.get_params().get('outputRate')

	def set_outputRate(self, outputRate):
		self.add_param('outputRate', outputRate)

