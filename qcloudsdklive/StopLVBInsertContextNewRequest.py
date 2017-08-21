#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StopLVBInsertContextNewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'StopLVBInsertContextNew', 'live.api.qcloud.com')

	def get_channelId(self):
		return self.get_params().get('channelId')

	def set_channelId(self, channelId):
		self.add_param('channelId', channelId)

	def get_actionId(self):
		return self.get_params().get('actionId')

	def set_actionId(self, actionId):
		self.add_param('actionId', actionId)

