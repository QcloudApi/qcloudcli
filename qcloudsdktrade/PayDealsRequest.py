#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class PayDealsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'trade', 'qcloudcliV1', 'PayDeals', 'trade.api.qcloud.com')

	def get_dealIds(self):
		return self.get_params().get('dealIds')

	def set_dealIds(self, dealIds):
		self.add_param('dealIds', dealIds)
		