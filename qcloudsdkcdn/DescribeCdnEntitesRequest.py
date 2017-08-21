#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeCdnEntitesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'DescribeCdnEntites', 'cdn.api.qcloud.com')

	def get_entityBaseDir(self):
		return self.get_params().get('entityBaseDir')

	def set_entityBaseDir(self, entityBaseDir):
		self.add_param('entityBaseDir', entityBaseDir)

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)
