#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class QueryBmTaskResultRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vpc', 'qcloudcliV1', 'QueryBmTaskResult', 'vpc.api.qcloud.com')

	def get_taskId(self):
		return self.get_params().get('taskId')

	def set_taskId(self, taskId):
		self.add_param('taskId', taskId)

