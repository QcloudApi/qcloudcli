#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteCdnEntityRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'DeleteCdnEntity', 'cdn.api.qcloud.com')

	def get_entityFileName(self):
		return self.get_params().get('entityFileName')

	def set_entityFileName(self, entityFileName):
		self.add_param('entityFileName', entityFileName)

