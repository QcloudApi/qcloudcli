#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UpdateCacheRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'UpdateCache', 'cdn.api.qcloud.com')

	def get_cache(self):
		return self.get_params().get('cache')

	def set_cache(self, cache):
		self.add_param('cache', cache)

	def get_hostId(self):
		return self.get_params().get('hostId')

	def set_hostId(self, hostId):
		self.add_param('hostId', hostId)

