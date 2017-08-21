#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ResizeRedisRequest(Request):

	def __init__(self):
		Request.__init__(self, 'redis', 'qcloudcliV1', 'ResizeRedis', 'redis.api.qcloud.com')

	def get_agentPay(self):
		return self.get_params().get('agentPay')

	def set_agentPay(self, agentPay):
		self.add_param('agentPay', agentPay)

	def get_payer(self):
		return self.get_params().get('payer')

	def set_payer(self, payer):
		self.add_param('payer', payer)

	def get_redisId(self):
		return self.get_params().get('redisId')

	def set_redisId(self, redisId):
		self.add_param('redisId', redisId)

	def get_memsize(self):
		return self.get_params().get('memsize')

	def set_memsize(self, memsize):
		self.add_param('memsize', memsize)

