#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyRedisProjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'redis', 'qcloudcliV1', 'ModifyRedisProject', 'redis.api.qcloud.com')

	def get_redisIds(self):
		return self.get_params().get('redisIds')

	def set_redisIds(self, redisIds):
		self.add_param('redisIds', redisIds)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

