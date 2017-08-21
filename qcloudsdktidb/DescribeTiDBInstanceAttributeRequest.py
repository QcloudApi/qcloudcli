#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeTiDBInstanceAttributeRequest(Request):

	def __init__(self):
		Request.__init__(self, 'tidb', 'qcloudcliV1', 'DescribeTiDBInstanceAttribute', 'tidb.api.qcloud.com')

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)

