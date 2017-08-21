#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ClearRedisRequest(Request):

	def __init__(self):
		Request.__init__(self, 'redis', 'qcloudcliV1', 'ClearRedis', 'redis.api.qcloud.com')

	def get_redisId(self):
		return self.get_params().get('redisId')

	def set_redisId(self, redisId):
		self.add_param('redisId', redisId)

	def get_password(self):
		return self.get_params().get('password')

	def set_password(self, password):
		self.add_param('password', password)

