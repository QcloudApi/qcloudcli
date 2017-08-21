#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyCdbCharsetRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdb', 'qcloudcliV1', 'ModifyCdbCharset', 'cdb.api.qcloud.com')

	def get_cdbInstanceIds(self):
		return self.get_params().get('cdbInstanceIds')

	def set_cdbInstanceIds(self, cdbInstanceIds):
		self.add_param('cdbInstanceIds', cdbInstanceIds)

	def get_charset(self):
		return self.get_params().get('charset')

	def set_charset(self, charset):
		self.add_param('charset', charset)

