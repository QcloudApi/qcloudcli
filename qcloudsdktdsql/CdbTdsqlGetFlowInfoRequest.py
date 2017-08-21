#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CdbTdsqlGetFlowInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'tdsql', 'qcloudcliV1', 'CdbTdsqlGetFlowInfo', 'tdsql.api.qcloud.com')

	def get_flowId(self):
		return self.get_params().get('flowId')

	def set_flowId(self, flowId):
		self.add_param('flowId', flowId)

