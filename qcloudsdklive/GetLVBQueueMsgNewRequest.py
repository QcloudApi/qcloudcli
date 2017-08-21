#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetLVBQueueMsgNewRequest(Request):

	def __init__(self):
		Request.__init__(self, 'live', 'qcloudcliV1', 'GetLVBQueueMsgNew', 'live.api.qcloud.com')

	def get_bid(self):
		return self.get_params().get('bid')

	def set_bid(self, bid):
		self.add_param('bid', bid)

	def get_count(self):
		return self.get_params().get('count')

	def set_count(self, count):
		self.add_param('count', count)

