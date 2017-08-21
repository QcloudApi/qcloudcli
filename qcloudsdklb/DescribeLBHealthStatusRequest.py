#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeLBHealthStatusRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'DescribeLBHealthStatus', 'lb.api.qcloud.com')

	def get_loadBalanceId(self):
		return self.get_params().get('loadBalanceId')

	def set_loadBalanceId(self, loadBalanceId):
		self.add_param('loadBalanceId', loadBalanceId)

	def get_listenerId(self):
		return self.get_params().get('listenerId')

	def set_listenerId(self, listenerId):
		self.add_param('listenerId', listenerId)

