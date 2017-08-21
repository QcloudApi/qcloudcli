#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RenewCbsStorageRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cbs', 'qcloudcliV1', 'RenewCbsStorage', 'cbs.api.qcloud.com')

	def get_storageId(self):
		return self.get_params().get('storageId')

	def set_storageId(self, storageId):
		self.add_param('storageId', storageId)

	def get_period(self):
		return self.get_params().get('period')

	def set_period(self, period):
		self.add_param('period', period)

