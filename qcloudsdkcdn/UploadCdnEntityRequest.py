#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class UploadCdnEntityRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'UploadCdnEntity', 'cdn.api.qcloud.com')

	def get_entityFileName(self):
		return self.get_params().get('entityFileName')

	def set_entityFileName(self, entityFileName):
		self.add_param('entityFileName', entityFileName)

	def get_entityFileMd5(self):
		return self.get_params().get('entityFileMd5')

	def set_entityFileMd5(self, entityFileMd5):
		self.add_param('entityFileMd5', entityFileMd5)
		
	def get_entityFile(self):
		return self.get_params().get('entityFile')

	def set_entityFile(self, entityFile):
		self.add_param('entityFile', entityFile)

