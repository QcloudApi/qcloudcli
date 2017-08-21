#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RenewRedisInquiryPriceRequest(Request):

	def __init__(self):
		Request.__init__(self, 'redis', 'qcloudcliV1', 'RenewRedisInquiryPrice', 'redis.api.qcloud.com')

	def get_redisId(self):
		return self.get_params().get('redisId')

	def set_redisId(self, redisId):
		self.add_param('redisId', redisId)

	def get_timeSpan(self):
		return self.get_params().get('timeSpan')

	def set_timeSpan(self, timeSpan):
		self.add_param('timeSpan', timeSpan)

