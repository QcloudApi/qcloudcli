#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DetachCbsStoragesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cbs', 'qcloudcliV1', 'DetachCbsStorages', 'cbs.api.qcloud.com')

	def get_storageIds(self):
		return self.get_params().get('storageIds')

	def set_storageIds(self, storageIds):
		self.add_param('storageIds', storageIds)

