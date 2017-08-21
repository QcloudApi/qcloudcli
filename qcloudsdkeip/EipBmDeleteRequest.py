#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class EipBmDeleteRequest(Request):

	def __init__(self):
		Request.__init__(self, 'eip', 'qcloudcliV1', 'EipBmDelete', 'eip.api.qcloud.com')

	def get_eipIds(self):
		return self.get_params().get('eipIds')

	def set_eipIds(self, eipIds):
		self.add_param('eipIds', eipIds)

	def get_eipIds(self):
		return self.get_params().get('eipIds')

	def set_eipIds(self, eipIds):
		self.add_param('eipIds', eipIds)

