#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RenameCdnEntityRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'RenameCdnEntity', 'cdn.api.qcloud.com')

	def get_entityFileName(self):
		return self.get_params().get('entityFileName')

	def set_entityFileName(self, entityFileName):
		self.add_param('entityFileName', entityFileName)
		
	def get_entityNewFileName(self):
		return self.get_params().get('entityNewFileName')

	def set_entityNewFileName(self, entityNewFileName):
		self.add_param('entityNewFileName', entityNewFileName)

