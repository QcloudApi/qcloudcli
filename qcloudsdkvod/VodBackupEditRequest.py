#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class VodBackupEditRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'VodBackupEdit', 'vod.api.qcloud.com')

	def get_fileId(self):
		return self.get_params().get('fileId')

	def set_fileId(self, fileId):
		self.add_param('fileId', fileId)

	def get_expireTime(self):
		return self.get_params().get('expireTime')

	def set_expireTime(self, expireTime):
		self.add_param('expireTime', expireTime)

