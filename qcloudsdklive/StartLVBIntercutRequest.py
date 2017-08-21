#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class StartLVBIntercutRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'StartLVBIntercut', 'live.api.qcloud.com')

	def get_channelIds(self):
		return self.get_params().get('channelIds')

	def set_channelIds(self, channelIds):
		self.add_param('channelIds', channelIds)

	def get_intercutType(self):
		return self.get_params().get('intercutType')

	def set_intercutType(self, intercutType):
		self.add_param('intercutType', intercutType)

	def get_intercutSource(self):
		return self.get_params().get('intercutSource')

	def set_intercutSource(self, intercutSource):
		self.add_param('intercutSource', intercutSource)

