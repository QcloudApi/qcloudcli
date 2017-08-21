#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class QueryUserPortraitForRetrieveRequest(Request):

	def __init__(self):
		Request.__init__(self, 'opc', 'qcloudcliV1', 'QueryUserPortraitForRetrieve', 'opc.api.qcloud.com')

	def get_fromType(self):
		return self.get_params().get('fromType')

	def set_fromType(self, fromType):
		self.add_param('fromType', fromType)

